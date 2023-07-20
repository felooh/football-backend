from django.db import models
import os
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

def get_upload_path(instance, filename):
    return os.path.join("images","blogger_images", str(instance.pk), filename)





class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    password = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to=get_upload_path, blank= True,null=True)
    gender = models.CharField(blank= True,max_length=15, null=True)
    mobile = models.IntegerField(blank= True, null=True)
    location = models.CharField(max_length=15,blank= True, null=True)
    occupation = models.CharField(max_length=255,blank= True, null=True)
    country = models.CharField(max_length=20,blank= True, null=True)
    username = models.EmailField(max_length=150, blank=True, null=True, unique=True)
    
    
    def __str__(self):
        return f"{self.first_name} | {self.username}"


