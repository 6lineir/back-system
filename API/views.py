from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
from accounts.models import User
# Create your views here.


class UserApi(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UsersApi(ListAPIView):
  serializer_class = UserSerializer
  def get_queryset(self):
    return User.objects.filter(pk = self.request)