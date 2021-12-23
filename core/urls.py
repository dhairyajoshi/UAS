from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('department-list/', core_views.DepartmentList.as_view(), name="department-list"),
    path('users-list/', core_views.UsersList.as_view(), name="users-list"),
    path('department-detail/<int:pk>/', core_views.DepartmentDetail.as_view(), name="department-detail"),
    path('user-profile', core_views.UserProfileView.as_view(), name="user-profile"),
]
