from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from django.contrib.auth.models import User

import core

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.Branch

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('password',)
        model = User
