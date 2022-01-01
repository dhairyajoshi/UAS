from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('department-list/', core_views.DepartmentList.as_view(), name="department-list"),
    path('department-detail/<int:pk>/', core_views.DepartmentDetail.as_view(), name="department-detail"),
    path('create-user/', core_views.CreateUserView.as_view(), name="create-user"),
    path('list-user/', core_views.ListUserView.as_view(), name="list-user"),
    path('user-detail/<int:pk>/', core_views.UserDetail.as_view(), name="user-detail"),
    path('user-profile/', core_views.UserProfileView.as_view(), name="user-profile"),
    path('create-address/',core_views.AddressCreate.as_view(),name="create-address"),
    path('student-application-list/',core_views.StudentApplicationListView.as_view(),name = "student-application-list"),
    path('application-status-update/',core_views.ApplicationStatusUpdate.as_view(),name = "application-status-update"),
    path('application-update-view/<int:id>/',core_views.UpdateStatusView.as_view(),name = "application-status-update"),
    path('list-academic/',core_views.ListAcademic.as_view(),name = "list-academic"),
    path('list-non-academic/',core_views.ListNonAcademic.as_view(),name = "list-non-academic"),
    path('create-education-detail/',core_views.EducationDetailCreate.as_view(),name = "education-detail-create")
]
