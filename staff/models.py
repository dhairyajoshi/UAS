from django.db import models
from core.models import Branch
from employee.models import Employee,Designation

# Create your models here.
class staff(models.Model):
    emp = models.OneToOneField(Employee,on_delete=models.CASCADE,null=True)
    desg =models.OneToOneField(Designation,on_delete =models.CASCADE,null = True)
    job_descr = models.CharField(max_length=100,null =True)
    curr_posn = models.CharField(max_length=50,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null= True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    class Meta:
        verbose_name_plural = "Staffs"