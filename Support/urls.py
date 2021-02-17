from django.urls import path
from .views import *

app_name = 'Support'
urlpatterns = [
    path('', Contact, name='contact'),

]
