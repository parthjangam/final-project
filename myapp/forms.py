from django import forms
from .models import Faculty, Subject, Class

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'unique_id']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'category', 'faculty']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['year', 'division']
