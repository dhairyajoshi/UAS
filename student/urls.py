from django.urls import path, include
from . import views as student_views

urlpatterns = [ 
    
    path('student-final-list/', student_views.StudentlListView.as_view(), name="student-final-list"),
    path('student-detail/<int:pk>/', student_views.StudentDetailView.as_view(), name="student-detail"),
    path('student-list/', student_views.StudentApplicationListView.as_view(), name="student-list"),
    path('student-application-detail/<int:pk>/', student_views.StudentApplicationDetailView.as_view(), name="student-application-detail"),

]
