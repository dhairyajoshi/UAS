from rest_framework import serializers
from . import models as employee_models



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('experiences', 'promotions','leaves_application','leave_records', 'slug')
        model = employee_models.Employee

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = employee_models.Designation

class ExperienceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = employee_models.Experience


class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields= '__all__'
        model= employee_models.LeaveApplication


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields= '__all__'
        model = employee_models.LeaveType
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = employee_models.role
