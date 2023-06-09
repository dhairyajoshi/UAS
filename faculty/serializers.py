from rest_framework import serializers
from . import models as faculty_models


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('slug', 'publications')
        model = faculty_models.Faculty

class PublicationCreationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = faculty_models.Publication