from django import forms
from django.forms import fields
from student.models import Student
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
    