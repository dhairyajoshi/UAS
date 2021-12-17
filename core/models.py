from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.fields import related
from django_countries.fields import CountryField
from django.conf import settings
# Create your models here.
GENDER_CHOICES=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHERS','OTHERS'),
)
CATEGORY_CHOICES=(
    ('General','General'),
    ('SC','ST'),
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
class User(AbstractUser):
    middle_name = models.CharField(max_length=50,null=True,blank=True),
    group_id = models.ForeignKey('UserGroup', on_delete=models.SET_NULL, null=True)
    education_details = models.ManyToManyField('EducationDetail', related_name='user_educationdetails')
    addresses = models.ManyToManyField('AddressDetail', related_name='user_addressdetails')
    date_of_birth = models.DateField(null=True)

    #Verify this
    user_group = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10, null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES, null=True)
    nationality = CountryField(null=True)
    religion = models.CharField(max_length=100,choices=RELIGION_CHOICES, null=True)
    blood_groups = models.CharField(max_length=10,choices=BLOOD_GROUPS, null=True)
    father_name = models.CharField(max_length=100,null=True,blank=True)
    mother_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    image = models.ImageField(upload_to='StudentPics', default='student_default.jpg')


    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta:
        verbose_name_plural = "Users"




class Branch(models.Model):
    name = models.CharField(max_length=100,null = True)
    code = models.CharField(max_length=10,null = True)
    year_of_esht = models.CharField(max_length = 4,null =True)
    is_academic = models.CharField(max_length=10,null= True)
    programme = models.ManyToManyField('Program',related_name='branch_programme')
    courses = models.CharField(max_length=100,null = True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Branchs"

class UserGroup(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
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
    class Meta:
        verbose_name_plural = "EducationDetails"


class EducationLevel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    class Meta:
        verbose_name_plural="EducationLevels"


class AddressDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_details', on_delete=models.SET_NULL, null=True)
    street_address = models.CharField(max_length = 100,blank = True, null = True)
    state = models.CharField(max_length = 100,blank = True, null = True)
    district = models.CharField(max_length = 100,blank = True, null = True)
    city = models.CharField(max_length = 100,blank = True, null = True)
    police_station = models.CharField(max_length = 100,blank = True, null = True)
    pin_code = models.CharField(max_length = 100,blank = True, null = True)
    address_type =  models.CharField(max_length = 100,blank = True, null = True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    # class Meta:
    #     verbose_name_plural = 'Address_Details'

class Program(models.Model):
    full_name = models.CharField(max_length= 100)
    short_name = models.CharField(max_length =10)
    year_of_esht = models.CharField(max_length =4)
    num_of_seats = models.IntegerField()
    is_ugc_accre = models.BooleanField(default= False)
    is_nb_accre = models.BooleanField(default= False)
    departments = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Programs"


