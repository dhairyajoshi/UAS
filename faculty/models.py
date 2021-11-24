from django.db import models
from core.models import Branch
from django.conf import settings


class Designation(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    designation=models.CharField(max_length=50)
    quaification=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    date_of_joining=models.DateField()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name



