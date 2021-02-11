from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','last_name','phone','codeMelli', 'referallcode','vip', 'is_staff', 'is_active')

admin.site.register(User, UserAdmin)