from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)

class Restaurant(models.Model):
    username = models.CharField(max_length=200,null=True)
    restaurant_groups = models.ManyToManyField(Group, related_name='restaurant_groups')
    USERNAME_FIELD = 'username'