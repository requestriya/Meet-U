from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    age = models.DateField()
    gender = models.CharField(max_length=50)
    

class User_images(models.Model):
    proimage = models.ForeignKey(User_Profile, default=None, on_delete=models.CASCADE)
    images2 = models.ImageField(null=True, blank=True)

