from django.contrib import admin
from .models import BlogPost
admin.site.site_header = "Gashnix Admin Dashboard"
# Register your models here.
admin.site.register(BlogPost)