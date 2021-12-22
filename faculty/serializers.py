from rest_framework import serializers
from . import models as faculty_models
from core import serializers as core_serializers


class FacultySerializer(serializers.ModelSerializer):
    user = core_serializers.UserSerializer(read_only=False)
    class Meta:
        fields = '__all__'
        model = faculty_models.Faculty

