from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Student,Faculty

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","first_name","last_name","email","user_type")

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("department","program_type","student_id")

class FacultyCreateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ("department","faculty_id")