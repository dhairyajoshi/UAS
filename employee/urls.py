from django.urls import path, include
from . import views as employee_views

urlpatterns = [
    path('employee-list/', employee_views.EmployeeList.as_view(), name="employees-list"),
    path('employee-detail/<int:pk>/', employee_views.EmployeeDetail.as_view(), name="employee-detail"),
    path('designation-list/',employee_views.DesignationList.as_view(),name="designation-list"),
    path('designation-detail/<int:pk>',employee_views.DesignationDetail.as_view(),name= "designation-detail"),
    path('experience-create/',employee_views.ExperienceCreate.as_view(),name = "Experience-creation"),
    path('role-list/',employee_views.Rolelist.as_view(),name = 'role-list'),
    path('role-detail/<int:id>/',employee_views.RoleDetail.as_view(),name = "role-detail")
]
