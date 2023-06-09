from django.db import models
from django.db.models.base import Model
from django.template.defaultfilters import slugify
from core.models import Department
from django.conf import settings
from employee.models import Employee


class Publication(models.Model):
    faculty = models.ForeignKey('Faculty',related_name="faculty_publication",on_delete=models.CASCADE,null= True,blank = True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200,null = True)

    
    def __str__(self):
        return self.name + '__' + self.description
    def save(self,*args,**kwargs):
        super(Publication,self).save(*args,**kwargs)
        curr_faculty = self.faculty
        curr_faculty.publications.add(self)
    class Meta:
        verbose_name_plural = "Publications"    

class Faculty(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    highest_qualification = models.CharField(max_length=50, null=True)
    specialization = models.CharField(max_length=50, null=True)
    teach_experience = models.IntegerField()
    publications = models.ManyToManyField(Publication,related_name = 'faculty_publications', blank=True)
    slug= models.SlugField(unique=True,blank=True)


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
        
    def save(self,*args,**kwargs):
        print(self.user)
        this_user = self.user
        this_employee = Employee.objects.get(user=this_user)
        self.employee = this_employee
        self.slug = slugify(self.user.first_name + '_' + self.user.last_name)
        slug_exists  = Faculty.objects.filter(slug = self.slug).exists()
        if slug_exists:
            self.slug += '_' + str(self.user.id)

        super(Faculty,self).save(*args,**kwargs)  

class hod_tenure(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
# class EducationDetails(models.Model):
#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name

