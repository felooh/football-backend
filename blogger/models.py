from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile_pic = models.ImageField(width_field="50",height_field="50",null=True)
    gender = models.CharField(max_length=15, null=True)
    mobile = models.IntegerField(null=True)
    location = models.CharField(max_length=15, null=True)
    occupation = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=20, null=True)
    
    
    username = None
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []