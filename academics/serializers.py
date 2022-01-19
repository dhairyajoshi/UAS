from dataclasses import fields
from rest_framework import serializers
from . import models as academics_models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = academics_models.Course