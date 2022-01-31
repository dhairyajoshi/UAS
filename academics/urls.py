from os import name
from django.urls import path, include
from . import views as academics_views
import academics

urlpatterns = [
    path('courses-list/',academics_views.CourseList.as_view(),name = "courses-list"),
    path('courses-detail/<int:id>/',academics_views.CourseDetail.as_view(),name = "course-detail"),
    path('program-list/',academics_views.ProgramList.as_view(),name='program-list'),
    path('program-detail/<int:id>/',academics_views.ProgramDetail.as_view(),name = "program-detail"),
]