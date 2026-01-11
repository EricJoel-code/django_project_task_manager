from django.shortcuts import render, redirect
#from django.http import  HttpResponse
from .models import Project, Task
# Create your views here.

def home(request):
    return render(request, 'home.html')


def projects_list(request):
    project = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': project
    })

def tasks_list(request):
    task = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks':task
    })