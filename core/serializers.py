from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from django.conf import settings
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.hashers import make_password
import core

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('user_permissions', 'groups', 'education_details','addresses')
        model = core_models.User



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.AddressDetail
        
class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.EducationLevel

class EducationSerializer(serializers.ModelSerializer):
      education_level = EducationLevelSerializer(read_only = True)
      class Meta:
          fields = '__all__'
          model = core_models.EducationDetail

        
class UserListSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    education_details = EducationSerializer(many = True,read_only = True)
    class Meta:
        # fields = '__all__'
        exclude = ('user_permissions', 'groups', 'password')
        model = core_models.User

class UserDetailSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many = True,read_only = True)
    education_details = EducationSerializer(many = True,read_only = True)
    class Meta:
        exclude = ('user_permissions', 'groups', 'password')
        model = core_models.User

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style = {'input_type':'password'})
    def authenticate(self,**kwargs):
        return authenticate(self.context['request'],**kwargs)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = None
        if email and password:
            if core_models.User.objects.filter(email = email).exists():
                user = self.authenticate(email = email,password = password)
            else:
                msg = {'detail':'Email address is not registered.','register':False}
                raise serializers.ValidationError(msg)
            if not user:
                msg={'detail':'Unable to log in with provided credentials.','register':True}
                raise serializers.ValidationError(msg,code = 'authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg,code = 'authorization')
        
        attrs['user'] = user
        return attrs
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user_permissions', 'groups', 'education_details','addresses')
        model = core_models.User
    def create(self, validated_data):
        password = validated_data.pop('password')
        user =  super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
