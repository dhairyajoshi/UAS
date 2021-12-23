from django.shortcuts import render
from . import models as faculty_models
from employee import models as employee_models
from core import models as core_models
from . import serializers as faculty_seralizers

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
from django.conf import settings

user_model = settings.AUTH_USER_MODEL

# Create your views here.

class FacultyRegistrationView(GenericAPIView):
    # queryset = faculty_models.Faculty.objects.all()
    # serializer_class = faculty_seralizers.FacultySerializer

    def post(self, request, *args, **kwargs):
        new_password = 'VSSUT'
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = new_password
        middle_name = request.data.get('middle_name')
        group_id = request.data.get('group_id')
        education_details = request.data.get('request.data.get')
        addresses = request.data.get('request.data.get')
        date_of_birth = request.data.get('request.data.get')
        user_group = request.data.get('user_group')
        gender = request.data.get('gender')
        category = request.data.get('category')
        nationality = request.data.get('nationality')
        religion = request.data.get('religion')
        blood_groups = request.data.get('blood_groups')
        father_name = request.data.get('father_name')
        mother_name = request.data.get('mother_name')
        phone_number = request.data.get('phone_number')
        image = request.data.get('image')

        new_user = user_model.objects.create_user(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
            middle_name = middle_name,
            group_id = group_id,
            education_details = education_details,
            addresses = addresses,
            date_of_birth = date_of_birth,
            user_group = user_group,
            gender = gender,
            category = category,
            nationality = nationality,
            religion = religion,
            blood_groups = blood_groups,
            father_name = father_name,
            mother_name = mother_name,
            phone_number = phone_number,
            image = image
        )

        new_employee = employee_models.Employee()
        new_employee.user = new_user
        new_employee.designation = request.data.get('desg')
        new_employee.post = request.data.get('post')
        new_employee.date_of_joining = request.data.get('date_of_joining')
        new_employee.date_of_leaving = request.data.get('date_of_leaving')
        new_employee.experiences = request.data.get('experiences')
        new_employee.work_phone_number = request.data.get('work_phone_number')
        new_employee.work_email_id = request.data.get('work_email_id')
        new_employee.pan_number = request.data.get('pan_number')
        new_employee.job_type = request.data.get('job_type')
        new_employee.promotions = request.data.get('promotions')
        new_employee.leaves = request.data.get('leaves')
        new_employee.save()


        new_faculty = faculty_models.Faculty()
        new_faculty.user = new_employee
        new_faculty.branch = request.data.get('branch')
        new_faculty.qualification = request.data.get('qualification')
        new_faculty.specialization = request.data.get('specialization')
        new_faculty.teach_experience = request.data.get('teach_experience')
        new_faculty.publications = request.data.get('publications')
        new_faculty.save()
        context = {
            "message": "new faculty created",
            # "faculty": faculty_seralizers.FacultySerializer(new_faculty),
            "new_password": new_password
        }

        return Response(context, status=HTTP_200_OK)