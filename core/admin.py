from django.contrib import admin
from .models import Department, EducationDetail, EducationLevel, User, UserGroup, AddressDetail

admin.site.register(Department)
admin.site.register(User)
admin.site.register(EducationDetail)
admin.site.register(AddressDetail)
admin.site.register(UserGroup)
admin.site.register(EducationLevel)

