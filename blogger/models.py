from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile_pic = models.ImageField(blank= True,null=True)
    gender = models.CharField(blank= True,max_length=15, null=True)
    mobile = models.IntegerField(blank= True, null=True)
    location = models.CharField(max_length=15,blank= True, null=True)
    occupation = models.CharField(max_length=255,blank= True, null=True)
    country = models.CharField(max_length=20,blank= True, null=True)
    
    
    username = None
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.first_name 
