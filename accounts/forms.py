from django import forms
from django.forms import ModelForm
from .models import User

class EditProfileForm(forms.ModelForm):
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
      "referallcode"
    )

class VertifyForm(forms.ModelForm):
    class Meta:
      model = User
      fields = (
        "imageVertify1",
         "imageVertify2"
      )