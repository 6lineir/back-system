from django.urls import path
from .views import *

app_name = 'Blog'
urlpatterns = [
    path('', index, name='Home'),

]
