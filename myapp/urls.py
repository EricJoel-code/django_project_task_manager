#from .views import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_list, name='projects_list'),
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('add_task/', views.add_task, name='add_task'),
]
