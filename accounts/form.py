from django import forms
from django.forms import ModelForm
from .models import User

class EditProfileForm(ModelForm):
  class Meta:
    model = User
    fields = (
      "last_name",
      "first_name",
      "email",
      "phone",
      "tphone",
      "telegram",
      "codeMelli",
      "addres",
      "imageVertify1",
      "imageVertify2",
      "referallcode"
    )