from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('branch-list', core_views.BranchList.as_view(), name="branch-list"),
]
