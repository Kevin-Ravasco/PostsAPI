from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import Post
from .serializers import PostSerializer


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_id='Create Post', operation_description='Create a new post'))
class CreatePostAPIView(CreateAPIView):
    """
    Endpoint to create posts

    url: api/posts/create/
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_id='Post Details', operation_description='Get the details of a post'))
@method_decorator(name='put', decorator=swagger_auto_schema(
    operation_id='Update Post', operation_description='Update a single post'))
@method_decorator(name='patch', decorator=swagger_auto_schema(
    operation_id='Update Post', operation_description='Update a single post'))
@method_decorator(name='delete', decorator=swagger_auto_schema(
    operation_id='Delete Post', operation_description='Delete a single post'))
class UpdateRetrieveDeletePostAPIView(RetrieveUpdateDestroyAPIView):
    """
    Endpoint to retrieve, update and delete a post

    url: api/posts/details/
    params: like=True
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_id='Post List', operation_description='Get A list of posts ordered by most recent'))
class PostsListAPIView(ListAPIView):
    """
    Endpoint to get the list of posts. They are ordered by most recent ones
    by default

    url: api/posts/
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


