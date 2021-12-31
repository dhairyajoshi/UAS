from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('department-list/', core_views.DepartmentList.as_view(), name="department-list"),
    path('department-detail/<int:pk>/', core_views.DepartmentDetail.as_view(), name="department-detail"),
    path('user-list/', core_views.UserList.as_view(), name="users-list"),
    path('user-detail/<int:pk>/', core_views.UserDetail.as_view(), name="user-detail"),
    path('user-profile/', core_views.UserProfileView.as_view(), name="user-profile"),
    path('create-address/',core_views.AddressCreate.as_view(),name="create-address"),
    path('application-pending-list/',core_views.StudentPendingApplicationListView.as_view(),name = "application-pending-list"),
    path('application-accepted-list/',core_views.StudentAcceptedApplicationListView.as_view(),name = "application-accepted-list"),
    path('application-rejected-list/',core_views.StudentRejectedApplicationListView.as_view(),name="application-rejected-list"),
    path('application-update-view/<int:id>/',core_views.UpdateStatusView.as_view(),name = "application-status-update")
]
