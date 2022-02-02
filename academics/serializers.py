from dataclasses import fields
from rest_framework import serializers
from . import models as academics_models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = academics_models.Course

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = academics_models.Program

class SemesterRecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = academics_models.SemesterRecord