from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='v1',
        description="API endpoints for the posts project. Find all information related to the routes included in the"
                    "project under this document."
        "\n\nThe `swagger-ui` view can be found [here](/api/docs/)."
        "\n\nThe `ReDoc` view can be found [here](/api/redoc/)."
        ,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="okevin182@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # our app urls
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),

    # to use drf browsable api
    path('api-auth/', include('rest_framework.urls')),

    # API Documentation
    path('api/docs/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
]
