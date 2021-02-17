from django.db import models
from accounts.models import User

class Ticket(models.Model):
    STATUS_CHOICES = (
		('n', 'جدید'),		 # new
		('p', "پاسخ داده شده"),		 # publish
		('i', "در حال بررسی"),	 # investigation
		('b', "بسته شده"), # Close
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)