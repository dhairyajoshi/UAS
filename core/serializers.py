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
        exclude = ('user_permissions', 'groups', 'education_details')
        model = core_models.User



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.AddressDetail
        
class UserListSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    class Meta:
        # fields = '__all__'
        exclude = ('user_permissions', 'groups', 'password')
        model = core_models.User


        