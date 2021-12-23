from django.urls import path, include
from . import views as employee_views

urlpatterns = [
    path('employees-list/', employee_views.EmployeeList.as_view(), name="employees-list"),
    path('employee-detail/<int:pk>/', employee_views.EmployeeDetail.as_view(), name="employee-detail"),
]
