#from .views import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_list, name='projects_list'),
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('add_project/', views.add_project, name='add_project'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('detail_project/<int:project_id>/', views.detail_project, name='detail_project')
]
