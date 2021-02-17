from django.contrib import admin
from .models import BlogPost
admin.site.site_header = "Gashnix Admin Dashboard"

class BlogAdmin(admin.ModelAdmin):
  list_display = ("title", "public", "publish")
  list_filter = ("public","publish")
  ordering = ['-publish', '-public']
  search_fields = ["title",]
# Register your models here.
admin.site.register(BlogPost, BlogAdmin)