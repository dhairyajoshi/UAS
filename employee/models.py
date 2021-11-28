from django.db import models
from core.models import Branch
from django.conf import settings
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
    post = models.CharField(max_length = 20),
    date_of_joining = models.DateField(null=True, blank=True)

