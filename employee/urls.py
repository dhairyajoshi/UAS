from django.urls import path, include
from . import views as employee_views

urlpatterns = [
    path('employee-list/', employee_views.EmployeeList.as_view(), name="employees-list"),
    path('employee-detail/<int:pk>/', employee_views.EmployeeDetail.as_view(), name="employee-detail"),
    path('designation-list/',employee_views.DesignationList.as_view(),name="designation-list"),
    path('designation-detail/<int:pk>',employee_views.DesignationDetail.as_view(),name= "designation-detail"),
    path('experience-create/',employee_views.ExperienceCreate.as_view(),name = "Experience-creation"),
    path('leavetype-create/',employee_views.LeaveTypeCreate.as_view(),name = "LeaveType-creation"),
    path('leave-create/',employee_views.LeaveCreate.as_view(),name = "Leave-creation"),
    path('employee-verify/',employee_views.VerifyEmployee.as_view(),name = "Employee-verification"),
    path('role-list/',employee_views.Rolelist.as_view(),name = 'role-list'),
    path('role-detail/<int:id>/',employee_views.RoleDetail.as_view(),name = "role-detail")
]
