from django.contrib import admin

# Register your models here.
from .models import Student, Student_Application


admin.site.register(Student)
admin.site.register(Student_Application)