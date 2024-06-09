from django.db import models
from . models import *

# Create your models here.
class employer(models.Model):
      firstname=models.CharField(max_length=100)
      lastname=models.CharField(max_length=100)
      position=models.CharField(max_length=100)
      company=models.CharField(max_length=100) 
      street=models.CharField(max_length=100)
      addimfor=models.CharField(max_length=100)
      pin=models.IntegerField
      place=models.CharField(max_length=100)
      country=models.CharField(max_length=100)
      code=models.IntegerField
      phonenumber=models.IntegerField
      email=models.EmailField
      password=models.CharField(max_length=100)