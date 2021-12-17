from django.contrib import admin
from .models import Branch, EducationDetail, EducationLevel, User, UserGroup

admin.site.register(Branch)
admin.site.register(User)
admin.site.register(EducationDetail)
# admin.site.register(AddressDetail)
admin.site.register(UserGroup)
admin.site.register(EducationLevel)

