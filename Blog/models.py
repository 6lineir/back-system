from django.db import models
from django.utils import timezone
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to='blog/%Y/%m/')
    public = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title