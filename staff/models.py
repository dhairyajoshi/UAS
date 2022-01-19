from django.db import models
from django.db.models.query_utils import select_related_descend
from django .template.defaultfilters import slugify
from core.models import Department
from employee.models import Employee,Designation

# Create your models here.
class staff(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    designation =models.ForeignKey(Designation,on_delete =models.CASCADE,null = True)
    job_description = models.CharField(max_length=100,null =True)
    current_position = models.CharField(max_length=50,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="Staff_department",null= True)

    slug = models.SlugField(unique= True,blank=True)
    def __str__(self):
        return self.employee.user.first_name +"_"+ self.designation.name
    
    def save(self,*args,**kwargs):
        curr_user = self.user
        curr_employee = Employee.objects.get(user = curr_user)
        self.employee = curr_employee
        curr_designation = self.employee.designation
        self.designation = curr_designation
        self.slug = slugify(self.job_description + '_' +self.current_position + '_'+ str(self.employee.id))
        super(staff,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = "Staffs"