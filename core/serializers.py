from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from django.contrib.auth.models import User

import core

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('password',)
        model = User
