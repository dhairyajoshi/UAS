from django.db import models 

from django.contrib.auth.models import User

class Faculty(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    faculty_branch=models.CharField(max_length=50)
    faculty_designation=models.CharField(max_length=50)
    faculty_quaification=models.CharField(max_length=50)
    faculty_specialization=models.CharField(max_length=50)
    faculty_phone_number=models.CharField(max_length=50)
    date_of_joining=models.CharField(max_length=50)

# Create your models here.

