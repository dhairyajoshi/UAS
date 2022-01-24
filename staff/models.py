from django.db import models
from django.db.models.query_utils import select_related_descend
from django .template.defaultfilters import slugify
from core.models import Department
from django.conf import settings
from employee.models import Employee,Designation
from core import models as core_models

class staff(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,related_name='staff_user_detail',null= True,blank= True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='staff_employee_detail',null = True,blank=True)
    designation =models.ForeignKey(Designation,on_delete =models.CASCADE,related_name='staff_Designation_detail',null = True,blank=True)
    job_description = models.CharField(max_length=100,null =True, blank=True)
    current_position = models.CharField(max_length=50,null=True, blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="Staff_department",null= True)

    slug = models.SlugField(unique= True,blank=True)
    def __str__(self):
        return self.employee.user.first_name +"_"+ self.designation.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.job_description + '_' +self.current_position + '_'+str(self.user.id))
        super(staff,self).save(*args,**kwargs)
        curr_user = self.user.id
        curr_employee = Employee.objects.get(user = core_models.User.objects.get(id =curr_user))
        self.employee = curr_employee
        curr_designation = self.employee.designation 
        self.designation = curr_designation
        self.slug = slugify(self.job_description + '_' +self.current_position + '_'+str(curr_employee))
        
        
    class Meta:
        verbose_name_plural = "Staffs"