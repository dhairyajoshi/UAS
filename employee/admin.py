from . models import Employee, LeaveApplication,Promotion,LeaveApplication,LeaveType,Designation,Experience,Account_Detail,role,LeaveRecord
from django.contrib import admin


admin.site.register(Employee)
admin.site.register(Promotion)
admin.site.register(LeaveApplication)
admin.site.register(LeaveRecord)
admin.site.register(LeaveType)
admin.site.register(Designation)
admin.site.register(Experience)
admin.site.register(Account_Detail)
admin.site.register(role)

# Register your models here.
