from django.contrib.auth import get_user_model

from .test_setup import TestSetup

User = get_user_model()


class TestModelManager(TestSetup):

    def test_createuser_method(self):
        user_credentials = {'email': 'user@gmail.com', 'password': 'password1'}
        user = User.objects.create_user(**user_credentials)
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_staff, False)
        self.assertEquals(user.is_admin, False)

    def test_create_user_with_invalid_data(self):
        user_credentials = {'email': '', 'password': ''}
        with self.assertRaises(ValueError):
            User.objects.create_user(user_credentials)

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

    def test_str_method(self):
        self.assertEquals(str(self.user_1), str(self.user_1.email))

    def test_has_perm_method(self):
        self.assertTrue(self.user_1.has_perm('read'))

    def test_has_module_perm_method(self):
        self.assertTrue(self.user_1.has_module_perms('accounts'))
