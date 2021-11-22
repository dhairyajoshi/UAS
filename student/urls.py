"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from baton.autodiscover import admin
from django.contrib import admin  
from django.urls import path, include
from . import views as employee_views

urlpatterns = [ 
    path('', employee_views.emp),  
    path('show/',employee_views.show),  
    path('show/edit/<int:id>', employee_views.edit),  
    path('update/<int:id>', employee_views.update),  
    path('show/delete/<int:id>', employee_views.destroy),
    path('show/generate/<int:id>', employee_views.generate_id),
    path('student-list', employee_views.StudentlList.as_view(), name="student-list"),

]
