from django.shortcuts import render
from django.template import context
from . import models as staff_models
from .import serializers as staff_serializers
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework import response
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView,ListCreateAPIView
from rest_framework.mixins import UpdateModelMixin
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import (
        SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, 
        BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny
    )
import random
import string
from django.conf import settings
from core import models as core_models

user_model = settings.AUTH_USER_MODEL
# Create your views here.

class StaffRegistration(ListCreateAPIView):
    queryset = staff_models.staff.objects.all()
    serializer_class = staff_serializers.StaffSerializer
    
    def post(self,request,*args,**kwargs):
        context = {}
        new_staff = staff_models.staff()
        new_staff.user = core_models.User.objects.get(id = request.data.get('user'))
        new_staff.current_position = request.data.get('current_position')
        new_staff.job_description = request.data.get('job_description')
        new_staff.department = core_models.Department(id = request.data.get('department'))
        new_staff.save()
        context['new_staff'] = staff_serializers.StaffSerializer(new_staff).data
        context['message'] = "New staff created successfully"
        return Response(context,status = HTTP_200_OK)