from distutils.command.upload import upload
from enum import unique
from pyexpat import model
from random import random
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.fields import related
from django_countries.fields import CountryField  
from django.conf import settings
import random
# Create your models here.
GENDER_CHOICES=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHERS','OTHERS'),
)
CATEGORY_CHOICES=(
    ('General','General'),
    ('SC','SC'),
    ('ST','ST'),
    ('OBC','OBC'),
    ('SEBC','SEBC'),
)
RELIGION_CHOICES = (
    ("HINDU","HINDU"),
    ("CHRISTIAN","CHRISTIAN"),
    ("MUSLIM","MUSLIM"),
    ("SIKH","SIKH"),
    ("JAIN","JAIN"),
    ("PARSI","PARSI"),
    ("BUDDHIST","BUDDHIST"),
    ("JEWISH","JEWISH"),
    ("JEWSIH","JEWISH")
)
BLOOD_GROUPS = (
    ("A+","A+"),
    ("B+","B+"),
    ("AB+","AB+"),
    ("O+","O+"),
    ("A-","A-"),
    ("B-","B-"),
    ("AB-","AB-"),
    ("O-","O-")
)
ADDRESS_TYPE_CHOICES = (
    ('Present', 'Present'),
    ('Permanent', 'Permanent')
)

def userFile(instance,filename):
    return '/'.join(['user',str(instance.id),filename])

def departmentFile(instance,filename):
    return '/'.join(['department',str(instance.id),filename])
class User(AbstractUser):
    middle_name = models.CharField(max_length=50,null=True,blank=True)
    group_id = models.ForeignKey('UserGroup', on_delete=models.SET_NULL, null=True, blank=True)
    education_details = models.ManyToManyField('EducationDetail', related_name='user_educationdetails', blank=True)
    addresses = models.ManyToManyField('AddressDetail', related_name='user_addressdetails', blank=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10, null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES, null=True)
    nationality = models.CharField(max_length = 100,null = True,blank=True)
    adhar_no = models.CharField(max_length=50,null = True,blank=True)
    religion = models.CharField(max_length=100,choices=RELIGION_CHOICES, null=True)
    blood_groups = models.CharField(max_length=10,choices=BLOOD_GROUPS, null=True)
    father_name = models.CharField(max_length=100,null=True,blank=True)
    mother_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    image = models.ImageField(upload_to=userFile, default='student_default.jpg',null = True,blank = True)
    slug = AutoSlugField(unique = True,populate_from = 'email')
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    



class Department(models.Model):
    name = models.CharField(max_length=100,null = True)
    code = models.CharField(max_length=10,null = True)
    year_of_esht = models.CharField(max_length = 4,null =True)
    is_academic = models.BooleanField(default= False)
    programme = models.ManyToManyField(to = 'academics.Program',related_name='branch_programme', blank=True)
    courses = models.ManyToManyField(to = 'academics.Course',related_name = 'Dept_courses', blank=True)
    image = models.ImageField(upload_to = departmentFile, default = 'department_default.jpg',null = True,blank = True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Departments"

class UserGroup(models.Model):
    name=models.CharField(max_length=100)
    site_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " (" + self.site_url + ")"
    class Meta:
        verbose_name_plural = "UserGroups"


class EducationDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_eucationdetails', on_delete=models.SET_NULL, null=True)

    ####verify......####
    education_level = models.ForeignKey('EducationLevel', on_delete=models.SET_NULL, null=True)
    college = models.CharField(max_length = 200, null = True, blank = True)
    board = models.CharField(max_length = 100, null = True, blank = True)
    total_cgpa = models.CharField(max_length = 10, null = True, blank = True)
    secured_cgpa = models.CharField(max_length = 10, null = True, blank = True)
    percentage = models.CharField(max_length = 10, null = True, blank = True)
    year_of_passing = models.CharField(max_length = 5, null = True, blank = True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    def save(self,*args,**kwargs):
        super(EducationDetail,self).save(*args,**kwargs)
        curr_user = self.user
        curr_user.education_details.add(self)
        
    class Meta:
        verbose_name_plural = "EducationDetails"


class EducationLevel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    
    def save(self,*args,**kwargs):
        super(EducationLevel,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural="EducationLevels"


class AddressDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_details', on_delete=models.CASCADE, blank=True)
    street_address = models.CharField(max_length = 100,blank = True, null = True)
    state = models.CharField(max_length = 100,blank = True, null = True)
    district = models.CharField(max_length = 100,blank = True, null = True)
    city = models.CharField(max_length = 100,blank = True, null = True)
    police_station = models.CharField(max_length = 100,blank = True, null = True)
    pin_code = models.CharField(max_length = 100,blank = True, null = True)
    address_type =  models.CharField(max_length = 100,choices =ADDRESS_TYPE_CHOICES,blank = True, null = True)

    def __str__(self):
        if self.user.first_name:
            return self.user.first_name + " " + self.user.middle_name + " " + self.user.last_name + " (" + self.user.email + ")"
        else:
            return self.user.username
    
    def save(self, *args, **kwargs):
        
        super(AddressDetail, self).save(*args, **kwargs)
        curr_user = self.user
        curr_user.addresses.add(self)