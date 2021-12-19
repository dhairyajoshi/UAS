from rest_framework import serializers
from . import models as employee_models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name')
        model = User


class EmployeeSerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=False)
    class Meta:
        # fields = '__all__'
        exclude = ('password')
        model = employee_models.Employee
