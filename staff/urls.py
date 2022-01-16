from django.urls import path, include
from . import views as staff_views

urlpatterns = [
    path('staff-list/',staff_views.StaffRegistration.as_view(),name="Staff-registration")
]
