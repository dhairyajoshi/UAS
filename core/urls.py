from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('department-list/', core_views.DepartmentList.as_view(), name="department-list"),
    path('department-detail/<int:pk>/', core_views.DepartmentDetail.as_view(), name="department-detail"),
    path('user-list/', core_views.UserList.as_view(), name="users-list"),
    path('user-detail/<int:pk>/', core_views.UserDetail.as_view(), name="user-detail"),
    path('user-profile/', core_views.UserProfileView.as_view(), name="user-profile"),
    path('create-address/',core_views.AddressCreate.as_view(),name="create-address")
]
