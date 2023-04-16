from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    phone = models.CharField(max_length=11,null=True,blank=True)
    government = models.CharField(max_length=50,null=True,blank=True)
    regon = models.CharField(max_length=50,null=True,blank=True)
    car_name = models.CharField(max_length=50,null=True,blank=True)
    car_model = models.CharField(max_length=200,null=True,blank=True)

    def _str_(self):
        return self.username