from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]
      