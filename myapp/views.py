from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import TaskForm
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
    
def add_task(request):
    
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
        
    return render(request, 'add_task.html', {'form': form})
