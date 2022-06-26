from django.urls import path
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'accounts'
urlpatterns = [
    path('user/<int:id>/', views.UpdateRetrieveDeleteUserView.as_view(), name='user_details'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', swagger_auto_schema(method='post', operation_id='Login User',
                                       operation_description='Login User')(obtain_auth_token)
         , name='login'),
]
