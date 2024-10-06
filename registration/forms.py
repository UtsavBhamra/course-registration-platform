from django import forms
from .models import Course

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("code","title","description","requested_students","accepted_students","instructors","schedule","department","credits")