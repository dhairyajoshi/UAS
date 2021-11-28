from django.db import models
from core.models import Branch
from django.conf import settings
from employee.models import Employee



class Designation(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Faculty(models.Model):
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    quaification = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    work_phone_number = models.CharField(max_length=12)
    work_email_id = models.CharField(max_length=100)
    
    


class hod_tenure(models.Model):
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE)

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE),
    is_active = models.BooleanField(),
    start_date = models.DateTimeField(),
    end_date = models.DateTimeField()

# class EducationDetails(models.Model):
#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name



