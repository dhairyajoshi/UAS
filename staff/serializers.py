from rest_framework import serializers
from rest_framework.settings import reload_api_settings
from . import models as staff_models
from employee import serializers as employee_serializers
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('slug',)
        model =staff_models.staff