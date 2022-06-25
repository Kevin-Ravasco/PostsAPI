from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from accounts.serializers import RegistrationSerializer, UserSerializer

User = get_user_model()


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_id='User Registration', operation_description='Create a new user account'))
class RegistrationView(CreateAPIView):
    """
    Endpoint for user Registration

    url: /api/accounts/register/
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_id='Get User Details', operation_description='Get the details of a user'))
@method_decorator(name='put', decorator=swagger_auto_schema(
    operation_id='Update User Details', operation_description='Update user information'))
@method_decorator(name='patch', decorator=swagger_auto_schema(
    operation_id='Update User Details', operation_description='Update user information'))
@method_decorator(name='delete', decorator=swagger_auto_schema(
    operation_id='Delete User', operation_description='Delete user'))
class UpdateRetrieveDeleteUserView(RetrieveUpdateDestroyAPIView):
    """
    Endpoint to get user details, to update user details and to
    delete the user

    url: /api/accounts/user/<int:id>/
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

