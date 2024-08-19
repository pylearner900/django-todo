from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic import ListView
from .models import Task
from django.urls import reverse_lazy

class index(ListView):
   model = Task
   template_name = "TodoApp/index.html"
   context_object_name = "tasks"
   
class CreateTask(CreateView):
    model = Task
    fields = "__all__"
    template_name = "TodoApp/createTask.html"
    success_url = reverse_lazy('index')
    
class UpdateTask(UpdateView):
    model = Task
    fields = "__all__"
    template_name = "TodoApp/createTask.html"
    success_url = reverse_lazy("index")
    
class DeleteTask(DeleteView):
    model = Task
    template_name = "TodoApp/deleteTask.html"
    success_url = reverse_lazy("index")
    context_object_name = "task"
