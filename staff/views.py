from django.shortcuts import render
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

user_model = settings.AUTH_USER_MODEL
# Create your views here.

class StaffRegistration(ListCreateAPIView):
    queryset = staff_models.staff.objects.all()
    serializer_class = staff_serializers.StaffSerializer
        
