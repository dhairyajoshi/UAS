from multiprocessing import context
from os import stat
import re
from urllib import request
from django.db.models import query
from django.shortcuts import get_object_or_404, render
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


class LeaveTypeCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset= employee_models.LeaveType.objects.all()
    serializer_class= employee_serializers.LeaveTypeSerializer

    def post(self,request,*args,**kwargs):
        if request.user.is_superuser == True:
            context = {}
            serializer = employee_serializers.LeaveTypeSerializer(data = request.data)
            if serializer.is_valid():
                new_leave_type = serializer.save()
                context['curr_leave_type'] = serializer.data
                return Response(context,status=HTTP_200_OK)
            else:
                return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        else:
            context={}
            context["errors"] = "You are not an administrator"
            return Response(context)

class LeaveCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset= employee_models.LeaveApplication.objects.all()
    serializer_class= employee_serializers.LeaveApplicationSerializer

    def post(self,request,*args,**kwargs):
        if request.user.group_id.id == 2 or request.user.group_id.id == 4:
            context ={}
            new_leave = employee_models.LeaveApplication()
            new_leave.start_date = request.data.get('start_date')
            new_leave.end_date = request.data.get("end_date")
            new_leave.description = request.data.get("description")
            new_leave.leave_address = request.data.get("leave_address")
            new_leave.leave_phone_number = request.data.get("leave_phone_number")
            leave_type_id= request.data.get("leave_type")
            new_leave.leave_type= employee_models.LeaveType.objects.get(id=leave_type_id)
            curr_user = request.user.id
            curr_employee = employee_models.Employee.objects.get(user =curr_user)
            new_leave.employee = curr_employee
            new_leave.save()
            curr_employee.leaves.add(new_leave)
            context["new_leave"] = employee_serializers.LeaveApplicationSerializer(new_leave).data
            context["message"] = "New leave application created successfully"
            return Response(context,status=HTTP_200_OK)
        else:
            context ={}
            context["errors"] = "You are not authorized."
            return Response(context,status = HTTP_400_BAD_REQUEST)

class VerifyEmployee(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class= employee_serializers.EmployeeSerializer


    def put(self,request, *args,**kwargs):
        if request.user.is_superuser ==True:
            context = {}
            emp_ids= map(int,request.data.get('emp_id').split(','))

            for emp_id in emp_ids:
                curr_emp= employee_models.Employee.objects.get(user=emp_id)
                curr_emp.verified_by=request.user
                curr_emp.save()
            context["message"]="Employee(s) verified successfully"
            return Response(context,status=HTTP_200_OK)
            
        else:
            context={}
            context["errors"] = "You are not an administrator"
            return Response(context)



class Rolelist(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = employee_models.role.objects.all()
    serializer_class = employee_serializers.RoleSerializer
    def post(self,request,*args,**kwargs):
        if request.user.is_superuser == True:
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
        if request.is_superuser == True:
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
        if request.user.is_superuser == True:
            context = {}
            curr_role = employee_models.role.objects.get(id =id)
            curr_role.delete()
            context["message"] = "Role deleted successfully"
            return Response(context,status= HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)
