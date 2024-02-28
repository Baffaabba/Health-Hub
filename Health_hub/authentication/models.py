from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password=None,**extra_fields):
        if not email:
            raise ValueError('The Email field is empty.')
    
        email = self.normalize_email(email)
        user = self.model(firstname=firstname, lastname=lastname, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, first_name='Admin', last_name='User', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(first_name, last_name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
class UserDetails(models.Model):
    user = models.OneToOneField('User', blank=True, null=True, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.email
    
    