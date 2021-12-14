from . models import Employee,Promotion,Leave,LeaveType
from django.contrib import admin


admin.site.register(Employee)
admin.site.register(Promotion)
admin.site.register(Leave)
admin.site.register(LeaveType)
# Register your models here.
