from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is empty.')
    
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'User'    
        verbose_name_plural = "User's"    
    
class UserDetails(models.Model):
    user = models.OneToOneField('CustomUser', blank=True, null=True, on_delete=models.CASCADE, related_name='details')
    age = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(default=1)
    region = models.CharField(max_length=5, choices=[
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ], default='north')
    is_diabetic = models.BooleanField(default=False)
    gain_weight = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.user.get_fullname()} {self.user.email}"
    
    class Meta:
        verbose_name = 'Details'    
        verbose_name_plural = "User Details"    