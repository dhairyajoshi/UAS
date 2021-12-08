from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('branch-list', core_views.BranchList.as_view(), name="branch-list"),
    path('branch-detail', core_views.BranchlDetail.as_view(), name="branch-detail"),
    path('user-profile', core_views.UserProfileView.as_view(), name="user-profile"),
]
