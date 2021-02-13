from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=12)
    tphone = models.CharField(max_length=12 ,blank=True)
    telegram = models.CharField(max_length=12 ,blank=True)
    codeMelli = models.CharField(max_length=16 ,blank=True)
    addres = models.CharField(max_length=600, blank=True)
    imageVertify1 = models.ImageField(blank=True, upload_to='User/%Y/%d/')
    imageVertify2 = models.ImageField(blank=True, upload_to='User/%Y/%d/')
    referallcode = models.CharField(max_length=12, blank=True)
    vip = models.BooleanField(default=False)
