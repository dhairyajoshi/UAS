from rest_framework import serializers
from . import models as employee_models
from core import serializers as core_serializers



class EmployeeSerializer(serializers.ModelSerializer):
    employee = core_serializers.UserSerializer(read_only=False)
    class Meta:
        # fields = '__all__'
        exclude = ('password')
        model = employee_models.Employee
