from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from django.conf import settings

import core

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('user_permissions', 'password', 'groups', 'education_details', 'addresses')
        model = core_models.User

class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = core_models.AddressDetail
    
    def save(self,*args,**kwargs):
        try:
            user = self.user
            super(core_models.AddressDetail,self).save(*args,**kwargs)
            user.addresses.add(self)
        except:
            super(AddressDetail,self).save(*args,**kwargs)

        
        