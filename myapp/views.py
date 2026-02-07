from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import TaskForm, ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

# Vista home de la web
@login_required
def home(request):
    return render(request, 'home.html')

# Vista para listar los proyectos
@login_required
def projects_list(request):
    project = Project.objects.filter(user=request.user)
    
    # Paginación de proyectos
    paginator = Paginator(project, 5) # Mostrar 5 proyectos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'projects/projects.html', context)

# Vista para listar las tareas
@login_required
def tasks_list(request):
    task = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html',{
        'tasks':task
    })
    
# Vista para añadir las tareas    
@login_required
def add_task(request):
    
    form = TaskForm(user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Tarea creada correctamnete')
            return redirect('add_task')
        
    return render(request, 'tasks/add_task.html', {'form': form})

# Vista para agregar los proyectos
@login_required
def add_project(request):
    
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False, user=request.user)
            project.user = request.user
            project.save()
            messages.success(request, 'Proyecto creado correctamente.')
            return redirect('add_project')
        
    return render(request, 'projects/add_project.html', {'form': form})
    
# Vista para eliminar las tareas
@login_required
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
    return redirect('tasks_list')

# Vista para completar las tareas
@login_required
def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.completed = not task.completed
        task.save()
    return redirect('tasks_list')

# Vista para ver el detalle de un proyecto
@login_required
def detail_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    
    task = project.tasks.all()
    
    return render(request, 'projects/detail_project.html', {
        'project': project,
        'tasks': task
    })
    
