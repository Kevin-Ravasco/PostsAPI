from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class TestModelManager(TestCase):
    def setUp(self):
        self.email = 'user@gmail.com'
        self.password1 = 'password1'
        self.password2 = 'password1'

    def test_createuser_method(self):
        user_credentials = {'email': 'user@gmail.com', 'password': 'password1'}
        user = User.objects.create_user(**user_credentials)
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_staff, False)
        self.assertEquals(user.is_admin, False)

    def test_createstaff_method(self):
        user_credentials = {'email': 'staff@gmail.com', 'password': 'password1'}
        user = User.objects.create_staffuser(**user_credentials)
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_staff, True)
        self.assertEquals(user.is_admin, False)

    def test_createsuperuser_method(self):
        user_credentials = {'email': 'superuser@gmail.com', 'password': 'password1'}
        user = User.objects.create_superuser(**user_credentials)
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_staff, True)
        self.assertEquals(user.is_admin, True)
        self.assertEquals(user.is_admin, True)


