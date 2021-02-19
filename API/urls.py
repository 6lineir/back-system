from django.urls import path, include
from .views import *

app_name = 'API'
urlpatterns = [
    path(r'users/', UserApi.as_view(), name="userApi"),
    path(r'users/<int:pk>', UsersApi.as_view(), name="usersApi"),
    path(r'', BlogApi.as_view(), name="blogApi"),
    path(r'<int:pk>', PostApi.as_view(), name="blogApi"),
]
