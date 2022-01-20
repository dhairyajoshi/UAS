from django.db.models import query
from django.shortcuts import render, redirect  
import random
import os
import datetime
import qrcode
from rest_framework import generics, serializers
from rest_framework import response
from rest_framework import status
from rest_framework.generics import GenericAPIView
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

from PIL import Image, ImageDraw, ImageFont

from student.forms import EmployeeForm
from student.models import Student
from employee.models import Employee
from . import models as student_models
from . import serializers as student_serializers
from core import serializers as core_serializers
from core import models as core_models


# Create your views here.  
class StudentlListView(generics.ListCreateAPIView):
    queryset = student_models.Student.objects.all()
    serializer_class = student_serializers.StudentSerializer

class StudentDetailView(generics.RetrieveDestroyAPIView):
    queryset = student_models.Student.objects.all()
    serializer_class = student_serializers.StudentApplicationSerializer

class StudentApplicationListView(generics.ListCreateAPIView):
    queryset = student_models.Student_Application.objects.all()
    serializer_class = student_serializers.StudentApplicationSerializer

class StudentApplicationDetailView(generics.RetrieveDestroyAPIView):
    queryset = student_models.Student_Application.objects.all()
    serializer_class = student_serializers.StudentApplicationSerializer



