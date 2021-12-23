from django.urls import path, include
from . import views as faculty_views

urlpatterns = [
    # path('faculty-registration/', faculty_views.FacultyRegistrationView.as_view(), name="faculty-registration"),
    path('faculty-list/', faculty_views.FacultyList.as_view(), name="faculty-list"),
    path('faculty-detail/<int:pk>/', faculty_views.FacultyDetail.as_view(), name="faculty-detail"),
]
