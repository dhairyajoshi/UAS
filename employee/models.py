from django.db import models
from django.db.models.fields import related
from django.template.defaultfilters import slugify
from django.conf import settings
from core.models import Department

# Create your models here.

class Designation(models.Model):
    name = models.CharField(max_length=50,null=True)
    pay = models.IntegerField(null=True)
    def __str__(self):
        return self.desg_name + '_' + str(self.pay)
    
    class Meta:
        verbose_name_plural = "Designations"

    
    def __str__(self):
        return self.name
class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    designation =models.ForeignKey(Designation,related_name='employee_designation',on_delete=models.CASCADE,null=True)
    post = models.CharField(max_length = 20,null= True)
    date_of_joining = models.DateField(null=True, blank=True)
    date_of_leaving = models.DateField(null=True,blank = True)
    experiences = models.ManyToManyField('Experience',related_name = 'employe_experience')
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
        self.slug = slugify(self.first_name+ '-' +self.last_name)
        slug_exists = Employee.objects.filter(slug=self.slug).exists()
        if slug_exists:
            self.slug +='-' +str(self.user.id)
        super(Employee,self).save(*args,**kwargs)

class Promotion(models.Model):
    emp = models.ForeignKey(Employee,related_name='emp_prmtion',on_delete = models.CASCADE,null =True)
    date = models.DateTimeField(null=True)
    previous_position = models.CharField(max_length=50,null=True)
    current_position = models.CharField(max_length=50,null = True)
    previous_salary=  models.IntegerField(null =True)
    current_salary = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Promotions"

class Leave(models.Model):
    employee = models.ForeignKey(Employee,related_name='Emp_leave',on_delete=models.CASCADE,null=True)
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
    leave = models.ForeignKey(Leave,related_name ='emp_leave_type', on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    class Meta:
        verbose_name_plural="LeaveTypes"

class Account_Detail(models.Model):
    employee =models.ForeignKey(Employee,related_name='Emp_account',on_delete =models.CASCADE,null=True)
    account_no = models.BigIntegerField(null = True)
    bank_name = models.CharField(max_length=50,null =True)
    branch_name = models.CharField(max_length=50,null =True)
    ifsc = models.CharField(max_length = 50,null =True)
    cif = models.CharField(max_length = 50,null =True)

    def __str__(self):
        return self.user.first_name + self.user.last_name
    
    class Meta:
        verbose_name_plural = "Account_Details"

class Experience(models.Model):
    employee = models.ForeignKey(Employee,related_name = 'employee_detail',on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    organisation_name =models.CharField(max_length=200,null=True)
    designation = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return self.user.first_name + "_" + self.user.last_name

class role(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee_role",null=True)
    name = models.CharField(max_length=50,null =True)
    start_date = models.DateField(null =True)
    end_date = models.DateField(null =True)
    description = models.CharField(max_length=100,null =True)

    def __str__(self):
        return self.user.first_name+ "_" + self.name
    
    class Meta:
        verbose_name_plural = "Roles"

