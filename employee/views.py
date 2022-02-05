from multiprocessing import context
import re
from django.db.models import query
from django.shortcuts import render
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
import random
import string
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from . import models as employee_models
from . import serializers as employee_serializers

# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset = employee_models.Employee.objects.all()
    serializer_class = employee_serializers.EmployeeSerializer
class EmployeeDetail(generics.RetrieveDestroyAPIView):
    queryset = employee_models.Employee.objects.all()
    serializer_class = employee_serializers.EmployeeSerializer

class DesignationList(generics.ListCreateAPIView):
    queryset = employee_models.Designation.objects.all()
    serializer_class = employee_serializers.DesignationSerializer

class DesignationDetail(generics.RetrieveDestroyAPIView):
    queryset = employee_models.Designation.objects.all()
    serializer_class = employee_serializers.DesignationSerializer

class ExperienceCreate(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = employee_serializers.ExperienceCreateSerializer

    def post(self,request,*args,**kwargs):
        context ={}
        new_experience = employee_models.Experience()
        new_experience.start_date = request.data.get('start_date')
        new_experience.end_date = request.data.get("end_date")
        new_experience.organisation_name = request.data.get("organisation_name")
        new_experience.designation = request.data.get("designation")
        curr_user = request.user.id
        curr_employee = employee_models.Employee.objects.get(user =curr_user)
        new_experience.employee = curr_employee
        new_experience.save()
        
        context["new_experience"] = employee_serializers.ExperienceCreateSerializer(new_experience).data
        context["message"] = "New experience created successfully"
        return Response(context,status=HTTP_200_OK)

class Rolelist(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = employee_models.role.objects.all()
    serializer_class = employee_serializers.RoleSerializer
    def post(self,request,*args,**kwargs):
        if request.user.group_id.id == 5:
            context = {}
            new_role = employee_models.role()
            new_role.employee = employee_models.Employee.objects.get(id = request.data.get("employee"))
            new_role.name = request.data.get("name")
            new_role.start_date = request.data.get("start_date")
            new_role.end_date = request.data.get("end_date")
            new_role.description = request.data.get("description")
            new_role.save()
            serializer = employee_serializers.RoleSerializer(new_role)
            context["New_role"] = serializer.data
            context["message"] = "New role created successfully"
            return Response(context,status = HTTP_200_OK)
        else:
            context ={}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)

class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = employee_models.role.objects.all()
    serializer_class = employee_serializers.RoleSerializer
    lookup_field = "id"
    def put(self,request,id,*args,**kwargs):
        if request.user.group_id.id == 5:
            context = {}
            curr_role = employee_models.role.objects.get(id =id)
            curr_role.employee = employee_models.Employee.objects.get(id = request.data.get("employee"))
            curr_role.name = request.data.get("name")
            curr_role.start_date = request.data.get("start_date")
            curr_role.end_date = request.data.get("end_date")
            curr_role.description = request.data.get("description")
            curr_role.save()
            serializer = employee_serializers.RoleSerializer(curr_role)
            context["Updated_role"] = serializer.data
            context["message"] = "Role Updated successfully"
            return Response(context,status = HTTP_200_OK)
        else:
            context ={}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)
    def delete(self,request,id,*args,**kwargs):
        if request.user.group_id.id == 5:
            context = {}
            curr_role = employee_models.role.objects.get(id =id)
            curr_role.delete()
            context["message"] = "Role deleted successfully"
            return Response(context,status= HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)