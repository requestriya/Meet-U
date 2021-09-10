from django.contrib import admin
from .models import *
# Register your models here.


class UserImageAdmin(admin.StackedInline):
    model = User_images

@admin.register(User_Profile)
class User_ProfileModelAdmin(admin.ModelAdmin):
    inlines = [UserImageAdmin]

    class Meta:
        model = User_Profile

@admin.register(User_images)
class UserImageAdmin(admin.ModelAdmin):
    pass

