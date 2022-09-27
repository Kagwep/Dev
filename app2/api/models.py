from email.policy import default
from django.db import models

# Create your models here.



class Task(models.Model):
    task_name = models.CharField(max_length = 200, blank =False, null = False)
    completed = models.BooleanField(default = False, blank = False, null = False)
    
    def __str__(self):
        return self.task_name
