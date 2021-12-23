from rest_framework import serializers
from . import models as employee_models



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('experiences', 'promotions', 'leaves')
        model = employee_models.Employee

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = employee_models.Designation