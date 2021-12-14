from . models import Employee,Promotion,Leave,LeaveType,Designation
from django.contrib import admin


admin.site.register(Employee)
admin.site.register(Promotion)
admin.site.register(Leave)
admin.site.register(LeaveType)
admin.site.register(Designation)


# Register your models here.
