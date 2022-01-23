from os import stat
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

class CourseList(generics.ListAPIView):
    queryset = academics_models.Course.objects.all()
    serializer_class = academics_serializers.CourseSerializer

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