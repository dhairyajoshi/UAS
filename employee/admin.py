from . models import Employee,Promotion,Leave,LeaveType,Designation,Experience,Account_Detail,role
from django.contrib import admin


admin.site.register(Employee)
admin.site.register(Promotion)
admin.site.register(Leave)
admin.site.register(LeaveType)
admin.site.register(Designation)
admin.site.register(Experience)
admin.site.register(Account_Detail)
admin.site.register(role)

# Register your models here.
