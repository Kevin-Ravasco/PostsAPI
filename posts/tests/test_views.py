from django.urls import reverse
from rest_framework import status

from .test_setup import TestSetup
from ..models import Post
from ..serializers import LIKE, UNLIKE


class TestCreatePostAPIView(TestSetup):
    def setUp(self) -> None:
        self.url = reverse('create_post')
        self.client.login(**self.user_1_credentials)

    def test_create_post(self):
        new_post_title = 'Some unique title here'
        data = {'title': new_post_title, 'content': 'some content'}
        response = self.client.post(self.url, data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Post.objects.filter(title=new_post_title).exists())

        # test post created_by has been populated by logged in user
        created_post = Post.objects.get(title=new_post_title)
        self.assertEqual(created_post.created_by, self.user_1)


class TestPostListAPIView(TestSetup):
    def setUp(self) -> None:
        self.url = reverse('posts')
        self.client.login(**self.user_1_credentials)

    def test_response_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 20)  # we have paginated by 20

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UpdateRetrieveDeletePostAPIView(TestSetup):
    def setUp(self) -> None:
        self.post = Post.objects.first()
        self.post_id = self.post.id  # we have a post with this id
        self.url = reverse('post_details', kwargs={'pk': self.post_id})
        self.client.login(**self.user_1_credentials)

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_post(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_retrieve_not_existing_post(self):
        non_existing_post_id = 999
        url = reverse('post_details', kwargs={'pk': non_existing_post_id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_post_details(self):
        new_title = 'New Title'
        new_content = 'New Content'
        data = {'title': new_title, 'content': new_content}
        response = self.client.put(self.url, data)
        # check post has been updated
        updated_post = Post.objects.get(id=self.post_id)
        self.assertEquals(updated_post.title, new_title)
        self.assertEquals(updated_post.content, new_content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_only_creator_allowed_to_update_post(self):
        # author of self.post is self.user_1, so we login as
        # user_2 and try to update it
        self.client.login(**self.user_2_credentials)
        new_title = 'New Title'
        new_content = 'New Content'
        data = {'title': new_title, 'content': new_content}
        response = self.client.put(self.url, data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_like_action(self):
        data = {'title': self.post.title, 'content': self.post.content, 'like_action': LIKE}
        response = self.client.put(self.url, data)
        self.post.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user_1.id in self.post.likes)

    def test_post_unlike_action(self):
        data = {'title': self.post.title, 'content': self.post.content, 'like_action': UNLIKE}

        # we add user_1 id in likes
        self.post.likes = [self.user_1.id]
        self.post.save()

        response = self.client.put(self.url, data)
        self.post.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # check user_1 id no longer in likes
        self.assertTrue(self.user_1.id not in self.post.likes)

    def test_delete_post(self):
        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        # check the user does not exist anymore
        self.assertFalse(Post.objects.filter(id=self.post_id).exists())
