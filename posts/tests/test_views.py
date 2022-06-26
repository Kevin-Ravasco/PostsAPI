from django.urls import reverse

from .test_setup import TestSetup
from ..models import Post


class TestPostListAPIView(TestSetup):
    def setUp(self) -> None:
        self.url = reverse('posts')
        self.client.login(**self.user_1_credentials)

    def test_response_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 20)  # we have paginated by 20

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)


class UpdateRetrieveDeletePostAPIView(TestSetup):
    def setUp(self) -> None:
        self.post_id = Post.objects.first().id  # we have a post with this id
        self.url = reverse('post_details', kwargs={'pk': self.post_id})
        self.client.login(**self.user_1_credentials)

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_retrieve_post(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_retrieve_not_existing_post(self):
        non_existing_post_id = 99
        url = reverse('post_details', kwargs={'pk': non_existing_post_id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_update_post_details(self):
        new_title = 'New Title'
        new_content = 'New Content'
        data = {'title': new_title, 'content': new_content}
        response = self.client.put(self.url, data)
        # check post has been updated
        updated_post = Post.objects.get(id=self.post_id)
        self.assertEquals(updated_post.title, new_title)
        self.assertEquals(updated_post.content, new_content)
        self.assertEquals(response.status_code, 200)

    def test_delete_post(self):
        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, 204)

        # check the user does not exist anymore
        self.assertFalse(Post.objects.filter(id=self.post_id).exists())
