from .models import AbstractUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = AbstractUser
        fields = ["username","password1","password2"]
        widgets = {
            "username":forms.TextInput(),
            "password":forms.Textarea(),
        }