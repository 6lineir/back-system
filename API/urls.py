from django.urls import path, include
from .views import *

app_name = 'API'
urlpatterns = [
    path(r'users/', UserApi.as_view(), name="userApi"),
    path(r'users/<int:pk>', UsersApi.as_view(), name="usersApi"),
    path(r'blog/', BlogApi.as_view(), name="blogApi"),
]
