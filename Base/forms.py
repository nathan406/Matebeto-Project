from .models import User,Customer,RestaurantOwner,Restaurant
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.db import transaction


# class CustomerSignUpForm(UserCreationForm):
#     # first_name = forms.CharField(required=True)
#     # last_name = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ["username","password1","password2"]
    
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_customer = True
#         user.save()
#         customer = Customer.objects.create(user=user)
#         customer.save()
#         return user

class CustomerSignUpForm(UserCreationForm):
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","password1","password2"]
    
    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return user


class RestaurantOwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","password1","password2"]

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_restaurantowner = True
        user.save()
        restaurantowner = RestaurantOwner.objects.create(user=user)
        restaurantowner.save()
        return user
