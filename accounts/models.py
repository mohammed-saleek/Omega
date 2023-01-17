from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=50,unique=True)
    username = models.CharField(max_length=40,unique=True)
    # is_customer = models.BooleanField(default=False)
    # is_employee = models.BooleanField(default=False)
    
    USERNAME_FIELD: 'email'
    # REQUIRED_FIELDS: ['username']
    
    def __str__(self):
        return self.username