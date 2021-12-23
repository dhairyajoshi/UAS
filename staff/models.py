from django.db import models
from django .template.defaultfilters import slugify
from core.models import Department
from employee.models import Employee,Designation

# Create your models here.
class staff(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE,null=True)
    designation =models.OneToOneField(Designation,on_delete =models.CASCADE,null = True)
    job_description = models.CharField(max_length=100,null =True)
    current_position = models.CharField(max_length=50,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="Staff_department",null= True)

    slug = models.SlugField(unique= True,blank=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.first_name + ' '+self.user.last_name)
        slug_exists = staff.objects.filter(slug = self.slug).exists()
        if slug_exists:
            self.slug +='_'+str(self.user.id)
        super(staff,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = "Staffs"