from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import TaskForm, ProjectForm
# Create your views here.

def home(request):
    return render(request, 'home.html')


def projects_list(request):
    project = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': project
    })

def tasks_list(request):
    task = Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks':task
    })
    
def add_task(request):
    
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
        
    return render(request, 'tasks/add_task.html', {'form': form})

def add_project(request):
    
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
        
    return render(request, 'projects/add_project.html', {'form': form})
    

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('tasks_list')

def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('tasks_list')

def detail_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/detail_project.html', {
        'project': project
    })