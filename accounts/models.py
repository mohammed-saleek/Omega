from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from accounts.manager import CustomUserManager
# Create your models here.

class LicenceType(models.Model):
    name = models.CharField(max_length=25)
    admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email',max_length=50,unique=True)
    username = models.CharField(max_length=40,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)
    token = models.CharField(max_length=255, null=True, blank=True)
    licence_type = models.ForeignKey(LicenceType, on_delete=models.CASCADE, blank=True, null=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS: ['username']
    
    def __str__(self):
        return self.username