# from django.urls import reverse
#
# from .test_setup import TestSetup
#
#
# class TestPostListAPIView(TestSetup):
#     def setUp(self) -> None:
#         self.url = reverse('posts')
#         self.client.login(**self.user_1_credentials)
#
#     def test_response_status(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
