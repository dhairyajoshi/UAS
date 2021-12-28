from rest_framework import serializers
from . import models as faculty_models


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user', 'slug', 'publications')
        model = faculty_models.Faculty

