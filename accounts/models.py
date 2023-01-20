from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email',max_length=50,unique=True)
    username = models.CharField(max_length=40,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)
    token = models.CharField(max_length=255, null=True, blank=True)
    
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS: ['username']
    
    def __str__(self):
        return self.username