from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from urllib3.connectionpool import xrange

from posts.models import Post

User = get_user_model()


class TestSetup(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_1_credentials = {'email': 'testemail@gmail.com', 'password': 'password123'}
        cls.user_2_credentials = {'email': 'testemail2@gmail.com', 'password': 'password123'}

        # create first test user
        cls.user_1 = User(email=cls.user_1_credentials['email'])
        cls.user_1.set_password(cls.user_1_credentials['password'])
        cls.user_1.save()

        # create second tes user
        cls.user_2 = User(email=cls.user_2_credentials['email'])
        cls.user_2.set_password(cls.user_2_credentials['password'])
        cls.user_2.save()

        # Create post objects for user 1
        for i in xrange(25):
            Post.objects.create(title=f'Some title {i}', content='some content', created_by=cls.user_1)
        return
