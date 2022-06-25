from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsListAPIView.as_view(), name='create_post'),
    path('create/', views.CreatePostAPIView.as_view(), name='create_post'),
    path('details/<int:id>/', views.UpdateRetrieveDeletePostAPIView.as_view(), name='create_post'),
]
