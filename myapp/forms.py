from django import forms
from .models import Task, Project

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user is not None:
            self.fields['project'].queryset = Project.objects.filter(user=user)        
                
                
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        