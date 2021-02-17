from rest_framework import serializers


from accounts.models import User



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'email', 'phone', 'vip')



# Blog Serlializers Api 
from Blog.models import BlogPost
class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    fields = ('__all__')