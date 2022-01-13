from django.urls import path, include
from . import views as staff_views

urlpatterns = [
    path('staff-registration/',staff_views.StaffRegistration.as_view(),name="Staff-registration")
]
