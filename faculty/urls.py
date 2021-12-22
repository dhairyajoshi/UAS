from django.urls import path, include
from . import views as faculty_views

urlpatterns = [
    path('faculty-registration/', faculty_views.FacultyRegistrationView.as_view(), name="faculty-registration"),
]
