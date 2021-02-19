from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import UserSerializer, BlogSerializer
from accounts.models import User
from Blog.models import BlogPost

# /api/users
class UserApi(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
# /api/users/<id>
class UsersApi(RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer




# Blog API Views /api/
class  BlogApi(ListAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogSerializer
# Blog API Views /api/<pk>
class  PostApi(RetrieveAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogSerializer