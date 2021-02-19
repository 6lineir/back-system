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
    # randnum = models.IntegerField(default=100)

    
    def __str__(self):
        return self.title
# # Add auto Number To randnum +1
#     def create(self,*args, **kwargs):
#         self.randnum = self.randnum +1
#         super(Ticket, self).create(*args, **kwargs)
        
      