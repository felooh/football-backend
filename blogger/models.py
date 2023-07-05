from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager



class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', email)
        return self._create_user(username=email, email=email, password=password, **extra_fields)



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
    username = models.CharField(max_length=150, default='', blank=True, null=True)

    
    objects = CustomUserManager()

     
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.first_name 


