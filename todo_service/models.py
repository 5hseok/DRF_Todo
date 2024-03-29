from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    completed_time = models.DateTimeField(auto_now=True)
    important = models.BooleanField(default=False)  
    
    def __str__(self):
        return self.title