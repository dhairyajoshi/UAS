"""vssut_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
#from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

    # Apps
    path('core/', include('core.urls')),
    path('staff/', include('staff.urls')),
    path('student/', include('student.urls')),
    path('faculty/', include('faculty.urls')),
    path('employee/', include('employee.urls')),

    # Authentication
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('django.contrib.auth.urls')),
]
