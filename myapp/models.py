from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    
    def __str__(self):
        return self.name
    
class Task (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.title + " - " + self.project.name