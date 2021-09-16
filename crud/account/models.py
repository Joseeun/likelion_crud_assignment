from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    email = models.TextField(max_length=500, null=True)
    phonenumber = models.TextField(max_length=20, null=True)