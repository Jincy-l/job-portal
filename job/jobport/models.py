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
      sus=models.BooleanField(default=True)


      
class employee(models.Model):
       firstname=models.CharField(max_length=100)
       lastname=models.CharField(max_length=100)
       Street=models.CharField(max_length=50)
       Pin=models.IntegerField()
       skills=models.CharField(max_length=100)
       highqua=models.CharField(max_length=100)
       job=models.CharField(max_length=100)
       city=models.CharField(max_length=100)
       country=models.CharField(max_length=100)
       code=models.IntegerField()
       phonenumber=models.IntegerField()
       email=models.EmailField()
       password=models.CharField(max_length=10)
       con=models.CharField(max_length=10)
       resume=models.FileField(upload_to='resume')
       image=models.ImageField(upload_to='p')
       sus=models.BooleanField(default=True)
       
       def __str__(self):
              return self.email
class postajob(models.Model):
       location=models.CharField(max_length=100)
       city=models.CharField(max_length=20)
       state=models.CharField(max_length=50)
       pincode=models.IntegerField() 
       
       jobtitle=models.CharField(max_length=50)
       jobdes=models.CharField(max_length=3000)
       jobtype=models.CharField(max_length=20)
       quali=models.CharField(max_length=50)
       schedule=models.CharField(max_length=20)
       numberof=models.IntegerField()
       image=models.ImageField(upload_to='pj')
       mail=models.CharField(max_length=100)
       company=models.CharField(max_length=100)
       pay=models.IntegerField()

class apply(models.Model):
       name=models.CharField(max_length=100) 
       # userid=models.IntegerField()
       jobid=models.CharField(max_length=50)
       email=models.EmailField()
       approved=models.BooleanField(default=False)
       rejected=models.BooleanField(default=False)
       applicant=models.ForeignKey(employee,on_delete=models.CASCADE)

class adminn(models.Model):
       name=models.CharField(max_length=100)
       email=models.EmailField()
       password=models.CharField(max_length=100)       


class msg(models.Model):
       name=models.CharField(max_length=100)
       email=models.EmailField()
       message=models.CharField(max_length=100)
       type=models.CharField(max_length=100)
       