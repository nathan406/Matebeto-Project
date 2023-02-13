from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurantowner = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class RestaurantOwner(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)


class Restaurant(models.Model):
    username = models.CharField(max_length=200,null=True)
    restaurant_groups = models.ManyToManyField(Group, related_name='restaurant_groups')
    USERNAME_FIELD = 'username'
    