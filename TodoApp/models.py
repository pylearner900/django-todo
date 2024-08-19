from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    detail = models.CharField(max_length=500,blank=True)
    publish = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.task
    