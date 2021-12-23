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

from . import models as core_models
from . import serializers as core_serializers

class DepartmentList(generics.ListCreateAPIView):
    queryset = core_models.Department.objects.all()
    serializer_class = core_serializers.DepartmentSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = core_models.User.objects.all()
    serializer_class = core_serializers.UserSerializer



class DepartmentDetail(generics.RetrieveDestroyAPIView):
    queryset = core_models.Department.objects.all()
    serializer_class = core_serializers.DepartmentSerializer



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        site = request.META['HTTP_ORIGIN']
        context = {}
        curr_user = request.user
        context['curr_user'] = core_serializers.UserSerializer(curr_user).data
        # # if site == 'https://authors.kanzulhaya.com' or site=='http://localhost:3000':
        #     # update_subscription()
        # author_qs = core_models.Writer.objects.filter(user=request.user)
        # if author_qs.exists():
        #     context['curr_author'] = core_serializers.WriterSerializer(author_qs[0]).data
        
        # all_articles = request.query_params.get('all_author_articles')
        # if all_articles:
        #     context['all_articles'] = core_serializers.ArticleSerializer(core_models.Article.objects.filter(writer=author_qs[0]), many=True).data
        
        # # elif site == 'https://kanzulhaya.com' or site=='http://localhost:3000':
        # user_active_plan = core_models.Subscription.objects.filter(user=curr_user, plan_active=True)
        # user_all_plans = core_models.Subscription.objects.filter(user=curr_user, plan_active=True)
        # user_free_trail = core_models.Subscription.objects.filter(user=curr_user, plan_id=1)

        # if user_active_plan.exists():
        #     context['user_active_plan'] = core_serializers.SubscriptionSerializer(user_active_plan[0]).data

        # context['user_all_plans'] = core_serializers.SubscriptionSerializer(user_all_plans, many=True).data
        # if user_free_trail.exists():
        #     context['user_free_trail'] = core_serializers.SubscriptionSerializer(user_free_trail[0]).data

        return Response(context, status=HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        context = {}
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        curr_user = request.user
        if username:
            curr_user.username = username
        if first_name:
            curr_user.first_name = first_name
        if last_name:
            curr_user.last_name = last_name
        if email:
            curr_user.email = email
        curr_user.save()
        context['curr_user'] = core_serializers.UserSerializer(curr_user).data
        # author_qs = core_models.Writer.objects.filter(user=request.user)
        # if author_qs.exists():
        #     curr_author = author_qs[0]
        #     serializer = core_serializers.WriterSerializer(curr_author, data=request.data, partial=True)
        #     if serializer.is_valid():
        #         serializer.save()
        #         context['curr_author'] = serializer.data
        #         return Response(context, status=HTTP_200_OK)
        #     else:
        #         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        return Response(context, status=HTTP_200_OK)



