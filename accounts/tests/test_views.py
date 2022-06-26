from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from accounts.tests.test_setup import TestSetup

User = get_user_model()


class TestSignupAPIView(TestSetup):
    def setUp(self):
        self.url = reverse('accounts:register')

    def test_signup_process(self):
        new_email = 'newemail23@gmail.com'
        data = {'email': new_email, 'password': 'password123',
                'password2': 'password123'}
        response = self.client.post(self.url, data, follow=True)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # we check a user with that new email has been created
        self.assertTrue(User.objects.filter(email=new_email).exists())

        # we check user token has been created
        new_user = User.objects.get(email=new_email)
        self.assertTrue(Token.objects.filter(user=new_user).exists())

    def test_with_unmatching_passwords(self):
        data = {'email': 'email@gmail.com', 'password': 'password125',
                'password2': 'password1255544'}
        response = self.client.post(self.url, data, follow=True)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestLoginAPIView(TestSetup):
    def setUp(self):
        self.url = reverse('accounts:login')

    def test_token_is_returned(self):
        credentials = {'username': self.user_1_credentials['email'],
                       'password': self.user_1_credentials['password']}
        response = self.client.post(self.url, credentials, follow=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)


class TestUpdateRetrieveDeleteUserAPIView(TestSetup):
    def setUp(self):
        self.user_id = self.user_1.id
        self.url = reverse('accounts:user_details', kwargs={'id': self.user_id})
        self.client.login(**self.user_1_credentials)

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_existing_user(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_retrieve_not_existing_user(self):
        not_existing_user_id = 34
        url = reverse('accounts:user_details', kwargs={'id': not_existing_user_id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_details(self):
        new_email = 'somenewemail@gmail.com'
        data = {'email': new_email}
        response = self.client.put(self.url, data)
        # check the new email has been updated
        self.assertEquals(User.objects.get(id=self.user_id).email, new_email)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        # check the user does not exist anymore
        self.assertFalse(User.objects.filter(id=self.user_id).exists())
