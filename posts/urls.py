from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostsListAPIView.as_view(), name='posts'),
    path('create/', views.CreatePostAPIView.as_view(), name='create_post'),
    path('details/<int:pk>/', views.UpdateRetrieveDeletePostAPIView.as_view(), name='post_details'),
    path('like-unlike/<int:pk>/', views.HandlePostLikeAPIView.as_view(), name='like_unlike'),
]
