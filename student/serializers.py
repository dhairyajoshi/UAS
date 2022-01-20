from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from django.contrib.auth.models import User
from . import models as student_models
from core import serializers as core_serialiers


class StudentApplicationSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=False)
    class Meta:
        fields = '__all__'
        model = student_models.Student_Application

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = student_models.Student


