from cgi import print_directory
from cgitb import lookup
from distutils import core
from os import stat
from shutil import register_unpack_format
from django.shortcuts import render
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
from . import models as academics_models
from . import serializers as academics_serializers
from core import models as core_models
# Create your views here.

class CourseList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = academics_models.Course.objects.all()
    serializer_class = academics_serializers.CourseSerializer
    def post(self,request,*args,**kwargs):
        if request.user.group_id.id == 5:
            context ={}
            new_course = academics_models.Course()
            new_course.course_code = request.data.get('course_code')
            new_course.subject = request.data.get('subject')
            new_course.credit = request.data.get('credit')
            new_course.contact_hours = request.data.get('contact_hours')
            new_course.course_type = request.data.get('course_type')
            curr_dept = core_models.Department.objects.get(id = request.data.get('department'))
            new_course.department = curr_dept
            new_course.save()
            curr_dept.courses.add(new_course)
            context["New_course"] = academics_serializers.CourseSerializer(new_course).data
            context["message"] = "Course created successfully"
            return Response(context,status= HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)


class ProgramList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = academics_models.Program.objects.all()
    serializer_class = academics_serializers.ProgramSerializer
    def post(self,request,*args,**kwargs):
        if request.user.group_id.id == 5:
            context = {}
            new_program = academics_models.Program()
            new_program.full_name = request.data.get("full_name")
            new_program.short_name = request.data.get("short_name")
            new_program.year_of_esht = request.data.get("year_of_esht")
            new_program.num_of_seats = request.data.get("num_of_seats")
            new_program.is_ugc_accredeted = request.data.get("is_ugc_accredeted")
            new_program.is_nb_accredeted = request.data.get("is_nb_accredeted")
            new_program.save()
            instance = academics_models.Program.objects.get(id = new_program.id)
            for dept in request.data.get("departments"):
                curr_dept = core_models.Department.objects.get(id = dept)
                instance.departments.add(curr_dept)
                curr_dept.programme.add(instance)
            context["New_program"] = academics_serializers.ProgramSerializer(instance).data
            context["message"] = "Program created successfully"
            return Response(context,status = HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)

class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = academics_models.Program.objects.all()
    serializer_class = academics_serializers.ProgramSerializer
    lookup_field = "id"
    def put(self,request,id,*args,**kwargs):
        if request.user.group_id.id ==5:
            instance = academics_models.Program.objects.get(id = id)
            instance.full_name = request.data.get("full_name")
            instance.short_name = request.data.get("short_name")
            instance.year_of_esht = request.data.get("year_of_esht")
            instance.num_of_seats = request.data.get("num_of_seats")
            instance.is_ugc_accredeted = request.data.get("is_ugc_accredeted")
            instance.is_nb_accredeted = request.data.get("is_nb_accredeted")
            for dept in request.data.get("departments"):
                curr_dept = core_models.Department.objects.get(id = dept)
                instance.departments.clear()
                instance.departments.add(curr_dept)
                curr_dept.programme.add(instance)
            instance.save()
            serializer = academics_serializers.ProgramSerializer(instance)
            return Response(serializer.data)
        else:
            context = {}
            context['errors'] = "You are not an administrator"
            return Response(context)
    def delete(self,request,id,*args,**kwargs):
        if request.user.group_id.id ==5:
            context={}
            instance = academics_models.Program.objects.get(id=id)
            instance.delete()
            context["message"] = "Program record deleted successfully"
            return Response(context,status=HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not administrator"
            return Response(context)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = academics_models.Course.objects.all()
    serializer_class = academics_serializers.CourseSerializer
    lookup_field = "id"
    def put(self,request,id,*args,**kwargs):
        if request.user.group_id.id ==5:
            context = {}
            instance = academics_models.Course.objects.get(id = id)
            instance.course_code = request.data.get("course_code")
            instance.subject = request.data.get("subject")
            instance.credit = request.data.get("credit")
            instance.contact_hours = request.data.get("contact_hours")
            curr_dept = instance.department
            instance.department = core_models.Department.objects.get(id = request.data.get("department"))
            if curr_dept != instance.department:
                dept_instance = core_models.Department.objects.get(id = curr_dept.id)
                dept_instance.courses.remove(instance)
                curr_dept = core_models.Department.objects.get(id = instance.department.id)
                curr_dept.courses.add(instance)
            instance.save()
            serializer = academics_serializers.CourseSerializer(instance)
            context["Current_course"] = serializer.data
            context["message"] = "Course Details updated successfully"
            return Response(context,status=HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not an administrator"
            return Response(context,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,*args,**kwargs):
        if request.user.group_id.id == 5:
            context = {}
            instance = academics_models.Course.objects.get(id = id)
            dept_instance = core_models.Department.objects.get(id = instance.department.id)
            dept_instance.courses.remove(instance)
            instance.delete()
            context["message"] = "Course record deleted successfully"
            return Response(context,status = HTTP_200_OK)
        else:
            context = {}
            context["errors"] = "You are not an administrator"
            return Response(context,status = HTTP_400_BAD_REQUEST)         

class SemesterRecordList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = academics_models.SemesterRecord.objects.all()
    serializer_class = academics_serializers.SemesterRecordSerializer
    def post(self,request,*args,**kwargs):
        if request.user.group_id.id == 5:
            context = {}
            new_semester_record = academics_models.SemesterRecord()
            new_semester_record.start_date = request.data.get('start_date')
            new_semester_record.end_date = request.data.get('end_date')
            new_semester_record.sem_type = request.data.get('sem_type')
            new_semester_record.department = core_models.Department.objects.get(id = request.data.get('department'))
            new_semester_record.save()
            context["New Semester Record"] = academics_serializers.SemesterRecordSerializer(new_semester_record).data
            context["message"] = "New semester record created successfully"
            return Response(context,status = HTTP_200_OK)
        else:
            context ={}
            context["errors"] = "You are not an administrator"
            return Response(context,status= HTTP_400_BAD_REQUEST)