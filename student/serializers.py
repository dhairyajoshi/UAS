from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from django.contrib.auth.models import User
from . import models as student_models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name')
        model = User

class StudentApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = student_models.Student_Application

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = student_models.Student
