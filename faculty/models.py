from django.db import models 

from django.contrib.auth.models import User

class Faculty(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    branch=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    quaification=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    date_of_joining=models.CharField(max_length=50)

# Create your models here.

