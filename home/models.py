from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(default='default.png', blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    interest = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)

    def get_photo(self):
        if self.dp and hasattr(self.dp, 'url'):
            return self.dp.url
        else:
            return "/static/images/default.png"
    

class User_images(models.Model):
    proimage = models.ForeignKey(User_Profile, default=None, on_delete=models.CASCADE)
    images2 = models.ImageField(null=True, blank=True)

