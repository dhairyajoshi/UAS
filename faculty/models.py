from django.db import models
from core.models import Branch
from django.conf import settings
from employee.models import Employee



class Designation(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Faculty(models.Model):
    empoyee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    designation = models.CharField(max_length=50, null=True)
    quaification = models.CharField(max_length=50, null=True)
    specialization = models.CharField(max_length=50, null=True)
    work_phone_number = models.CharField(max_length=12, null=True)
    work_email_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class hod_tenure(models.Model):
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

# class EducationDetails(models.Model):
#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name



