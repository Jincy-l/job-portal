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
      pin=models.IntegerField()
      place=models.CharField(max_length=100)
      country=models.CharField(max_length=100)
      code=models.IntegerField()
      phonenumber=models.IntegerField()
      email=models.EmailField()
      password=models.CharField(max_length=10)
      confirm=models.CharField(max_length=10)
      image=models.ImageField(upload_to='pic')


      
class employee(models.Model):
       first_name=models.CharField(max_length=100)
       last_name=models.CharField(max_length=100)
       Street=models.CharField(max_length=50)
       Pin=models.IntegerField()
       skills=models.CharField(max_length=100)
       highqua=models.CharField(max_length=100)
       job=models.CharField(max_length=100)
       place=models.CharField(max_length=100)
       country=models.CharField(max_length=100)
       code=models.IntegerField()
       phonenumber=models.IntegerField()
       email=models.EmailField()
       passworde=models.CharField(max_length=10)
       con=models.CharField(max_length=10)
class postajob(models.Model):
       location=models.CharField(max_length=100)
       city=models.CharField(max_length=20)
       area=models.CharField(max_length=50)
       pincode=models.IntegerField() 
       address=models.CharField(max_length=100)
       jobtitle=models.CharField(max_length=50)
       jobdes=models.CharField(max_length=500)
       jobtype=models.CharField(max_length=20)
       quali=models.CharField(max_length=50)
       schedule=models.CharField(max_length=20)
       numberof=models.IntegerField()
       image=models.ImageField(upload_to='pj')
       mail=models.CharField(max_length=100)