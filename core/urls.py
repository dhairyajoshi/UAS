from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('branch-list', core_views.BranchList.as_view(), name="branch-list"),
    path('user-profile', core_views.UserProfileView.as_view(), name="user-profile"),
]
