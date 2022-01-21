from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('department-list/', core_views.DepartmentList.as_view(), name="department-list"),
    path('department-detail/<int:id>/', core_views.DepartmentDetailView.as_view(), name="department-detail"),
    path('create-user/', core_views.CreateUserView.as_view(), name="create-user"),
    path('list-user/', core_views.ListUserView.as_view(), name="list-user"),
    path('user-detail/<int:pk>/', core_views.UserDetail.as_view(), name="user-detail"),
    path('user-profile/', core_views.UserProfileView.as_view(), name="user-profile"),
    path('create-address/',core_views.AddressCreate.as_view(),name="create-address"),
    path('student-application-list/',core_views.StudentApplicationListView.as_view(),name = "student-application-list"),
    path('application-status-update/',core_views.ApplicationStatusUpdate.as_view(),name = "application-status-update"),
    path('application-update-view/<int:id>/',core_views.UpdateStatusView.as_view(),name = "application-status-update"),
    path('create-education-detail/',core_views.EducationDetailCreate.as_view(),name = "education-detail-create"),
    path('education-detail-update/<int:id>/',core_views.EducationDetailUpdate.as_view(),name = "update-get-education-detail"),
    path('education-level-list/',core_views.EducationLevelView.as_view(),name='create-education-level'),
    path('education-level-detail/<int:id>/',core_views.EducationLevelDetailView.as_view(),name = 'education-level-detail'),
]
