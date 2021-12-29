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
def emp(request): 
    if request.method == "POST": 
        print(request.POST)
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/employee/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Student.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):
    

    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Student.objects.get(id=id)  
    employee.delete()  
    return redirect("/employee/show")
def generate_id(request,id):  
    # employee = Employee.objects.get(id=id)  
    # employee.delete()
    ex = Student.objects.get(id=id)
    #patient_edit = PatientInfo.objects.get(id=patient_id) # object to update
    ex.is_valid = True
    ex.save() # save objec
    #print(employees)
    print("employees are.......")
    print(ex.eemail)
    print("Generating ID")
    image = Image.new('RGB', (1000, 900), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
    (x, y) = (50, 50)
    # message = input('\nEnter Your Company Name: ')
    message="Veer Surendra Sai University of Technology"
    company = message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (300, 100)
    message="Burla, Odisha"
    company = message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (300, 150)
    message="Registration Card"
    company = message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=30)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 200)

    ########################################
    ### Make this field dynamic ########
    idno = random.randint(10000000, 90000000)

    #########################################
    message = str('Regd No: ' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=30)
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (50, 275)
    message = ex.fname+" "+ex.lname
    name = message
    message = str('Name: ' + str(message))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=30)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 350)
    message = "Male"
    message = str('Gender: ' + str(message))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 500)
    message = ex.days+" "+ex.month+" "+ex.year
    message = str('DOB: ' + str(message))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 650)
    message = "June 2025"
    temp = message
    message = str('Valid Upto: ' + str(message))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 750)
    message = ex.branch
    message = str('B. Tech: ' + str(message))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    # name=message


    image.save('media/'+str(name) + '.png')

    img = qrcode.make(
        {
            'Name':name,
            'Regd':idno,
            'Branch':ex.branch
        }
    )  # this info. is added in QR code, also add other things
    img.save('media/'+str(idno) + '.bmp')

    print(img)

    til = Image.open('media/'+name + '.png')
    im = Image.open('media/'+str(idno) + '.bmp')  # 25x25
    til.paste(im, (450, 250))
    til.save('media/'+name + '.pdf')


    
    return redirect("/employee/show")
  
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



