from django.db import models
from accounts.models import User


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    BTC_Address = models.CharField(max_length=200, blank=True)
    BTC_Amount = models.CharField(max_length=200, blank=True)
    LTC_Address = models.CharField(max_length=200, blank=True)
    LTC_Amount = models.CharField(max_length=200, blank=True)
    Doge_Address = models.CharField(max_length=200, blank=True)
    Doge_amount = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.user