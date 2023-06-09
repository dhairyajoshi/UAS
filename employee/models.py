from django.db import models
from django.db.models.fields import related
from django.template.defaultfilters import slugify
from django.conf import settings
from core.models import Department

JOB_TYPE_CHOICE = {
    ('Temporary', 'Temporary'),
    ('Permanent', 'Permanent')
}

class Designation(models.Model):
    name = models.CharField(max_length=50,null=True)
    short_name = models.CharField(max_length=10,null=True)
    pay = models.IntegerField(null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Designations"

    
    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    designation =models.ForeignKey(Designation,related_name='employee_designation',on_delete=models.SET_NULL, null=True)
    date_of_joining = models.DateField(null=True, blank=True)
    date_of_leaving = models.DateField(null=True,blank = True)
    experiences = models.ManyToManyField('Experience',related_name = 'employe_experience')
    work_phone_number = models.CharField(max_length=14, null=True)
    work_email_id =models.EmailField(max_length=100,null=True)
    pan_number = models.CharField(max_length= 15,null=True)
    job_type = models.CharField(choices=JOB_TYPE_CHOICE, max_length=50,null= True)
    promotions = models.ManyToManyField('Promotion',related_name = 'employee_promotion')
    leaves_application = models.ManyToManyField('LeaveApplication',related_name = 'employee_leave')
    leave_records = models.ManyToManyField('LeaveRecord',related_name="Employee_leave_record")
    
    slug = models.SlugField(unique=True,blank=True)


    def __str__(self):
        if self.user.first_name:
            return self.user.first_name + ' ' + self.user.last_name
        elif self.user.username:
            return self.user.username
        else:
            return self.user.email


    def save(self,*args,**kwargs):
        if self.user.first_name:
            self.slug = slugify(self.user.first_name+ '-' +self.user.last_name)
        else:
            self.slug = slugify(self.user.email.split('@')[0])
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

class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee,related_name='Emp_leave',on_delete=models.CASCADE,null=True)
    leave_type = models.ForeignKey('LeaveType',related_name ='emp_leave_type', on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null= True)
    end_date = models.DateField(null=True)
    is_halfday = models.BooleanField(default = False)
    approver = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null = True)
    is_granted = models.BooleanField(default=False)
    description = models.CharField(max_length=100,null=True)
    leave_address = models.CharField(max_length=50,null=True)
    leave_phone_number = models.CharField(max_length=12,null= True)

    def __str__(self):
        return str(self.leave_type.name) + '_' +str(self.employee.user.first_name) + ' ' +str(self.employee.user.last_name)
    
    class Meta:
        verbose_name_plural ="Leaves"

class LeaveRecord(models.Model):
    employee = models.ForeignKey(Employee,related_name = 'Leave_Record_Employee_Details',on_delete = models.CASCADE,null =True)
    leave_type = models.ForeignKey('LeaveType',related_name='Leave_Record_Type',on_delete=models.CASCADE,null = True)
    leave_days = models.IntegerField(default=0)
    leave_applications = models.ManyToManyField(LeaveApplication,related_name='Leave_Record_Applications')
    def __str__(self):
        return str(self.employee.user.first_name) + str(self.leave_type.name) + '_'+str(self.leave_days)
    class Meta:
        verbose_name_plural = "LeaveRecords"
class LeaveType(models.Model):
    name = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.name
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
        return str(self.start_date)+'_'+self.organisation_name+'_'+str(self.end_date)

    def save(self,*args,**kwargs):
        super(Experience,self).save(*args,**kwargs)
        curr_employee = self.employee
        curr_employee.experiences.add(self)
    
    class Meta:
        verbose_name_plural = "Experiences"
class role(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee_role",null=True)
    name = models.CharField(max_length=50,null =True)
    start_date = models.DateField(null =True)
    end_date = models.DateField(null =True)
    description = models.CharField(max_length=100,null =True)

    def __str__(self):
        return self.employee.user.first_name+ "_" + self.name
    
    class Meta:
        verbose_name_plural = "Roles"

