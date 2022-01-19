from django.urls import path, include
from . import views as academics_views
import academics

urlpatterns = [
    path('courses-list/',academics_views.CourseList.as_view(),name = "courses-list"),
]