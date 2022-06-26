from .test_setup import TestSetup
from ..models import Post


class TestPostModel(TestSetup):
    def setUp(self) -> None:
        self.post = Post.objects.first()

    def test_str_method(self):
        self.assertEqual(str(self.post), str(self.post.title))

    def test_likes_count_method(self):
        # self.post has no likes, ie likes = []
        self.assertEqual(self.post.likes_count, 0)
