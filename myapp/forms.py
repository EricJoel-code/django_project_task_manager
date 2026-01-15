from django import forms
from .models import Task, Project

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project']
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        