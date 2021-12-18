from . models import Employee,Promotion,Leave,LeaveType,Designation,Experience
from django.contrib import admin


admin.site.register(Employee)
admin.site.register(Promotion)
admin.site.register(Leave)
admin.site.register(LeaveType)
admin.site.register(Designation)
admin.site.register(Experience)

# Register your models here.
