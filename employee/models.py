from django.db import models
from core.models import Branch
from django.template.defaultfilters import slugify
from django.conf import settings
from core.models import Branch

# Create your models here.

class Designation(models.Model):
    name = models.CharField(max_length=50,null=True)
    pay = models.IntegerField(null=True)
    def __str__(self):
        return self.desg_name + '_' + str(self.basic_pay)
    
    class Meta:
        verbose_name_plural = "Designations"

    
    def __str__(self):
        return self.name
class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    desg =models.OneToOneField(Designation,on_delete=models.CASCADE,null=True)
    post = models.CharField(max_length = 20,null= True)
    date_of_joining = models.DateField(null=True, blank=True)
    date_of_leaving = models.DateField(null=True,blank = True)
    experiences = models.CharField(max_length=50,null =True)
    work_phone_number = models.CharField(max_length=12, null=True)
    work_email_id =models.EmailField(max_length=20,null=True)
    pan_number = models.CharField(max_length= 10,null=True)
    job_type = models.CharField(max_length=50,null= True)
    promotions = models.ManyToManyField('Promotion',related_name = 'employee_promotion')
    leaves = models.ManyToManyField('Leave',related_name = 'employee_leave')
    
    slug = models.SlugField(unique=True,blank=True)
    def __str__(self):
        return self.user.first_name + ' '+ self.user.last_name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.first_name+ '_-' +self.last_name)
        slug_exists = Employee.objects.filter(slug=self.slug).exists()
        if slug_exists:
            self.slug +='-' +str(self.user.id)
        super(Employee,self).save(*args,**kwargs)

class Promotion(models.Model):
    emp = models.OneToOneField(Employee,on_delete = models.CASCADE,null =True)
    date = models.DateTimeField(null=True)
    previous_posn = models.CharField(max_length=50,null=True)
    current_posn = models.CharField(max_length=50,null = True)
    prev_salary=  models.IntegerField(null =True)
    curr_salary = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Promotions"

class Leave(models.Model):
    emp = models.OneToOneField(Employee,on_delete=models.CASCADE)
    start_date = models.DateField(null= True)
    end_date = models.DateField(null=True)
    is_granted = models.BooleanField(default=False)
    description = models.CharField(max_length=100,null=True)
    leave_address = models.CharField(max_length=50,null=True)
    leave_phone_number = models.CharField(max_length=12,null= True)

    def __str__(self):
        return self.user.first_name + ' ' + self. user.last_name
    
    class Meta:
        verbose_name_plural ="Leaves"

class LeaveType(models.Model):
    leave = models.ForeignKey(Leave,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    class Meta:
        verbose_name_plural="LeaveTypes"

class Account_Detail(models.Model):
    emp =models.ForeignKey(Employee,on_delete =models.CASCADE,null=True)
    account_no = models.BigIntegerField(null = True)
    bank_name = models.CharField(max_length=50,null =True)
    branch_name = models.CharField(max_length=50,null =True)
    ifsc = models.CharField(max_length = 50,null =True)
    cif = models.CharField(max_length = 50,null =True)

    def __str__(self):
        return self.user.first_name + self.user.last_name
    
    class Meta:
        verbose_name_plural = "Account_Details"


