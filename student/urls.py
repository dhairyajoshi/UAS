from django.urls import path, include
from . import views as employee_views

urlpatterns = [ 
    path('', employee_views.emp),  
    path('show/',employee_views.show),  
    path('show/edit/<int:id>', employee_views.edit),  
    path('update/<int:id>', employee_views.update),  
    path('show/delete/<int:id>', employee_views.destroy),
    path('show/generate/<int:id>', employee_views.generate_id),
    path('student-list', employee_views.StudentlList.as_view(), name="student-list"),

]
