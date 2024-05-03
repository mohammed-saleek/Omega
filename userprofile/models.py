from django.db import models
from accounts.models import User
# from django.conf import settings

# Create your models here.
class EducationDetails(models.Model):
    name = models.CharField(max_length=50)
    graduation_year = models.IntegerField()


class ProfessionDetails(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)


class Address(models.Model):
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    education = models.ForeignKey(EducationDetails, on_delete=models.CASCADE, blank=True, null=True)
    profession = models.ForeignKey(ProfessionDetails, on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)