from django.contrib import admin
from .models import Address_Detail, Branch, EducationDetail, EducationLevel, User, UserGroup

admin.site.register(Branch)
admin.site.register(User)
admin.site.register(EducationDetail)
admin.site.register(Address_Detail)
admin.site.register(UserGroup)
admin.site.register(EducationLevel)

