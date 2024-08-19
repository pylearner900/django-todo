from django.urls import path
from .views import index,CreateTask,UpdateTask,DeleteTask

urlpatterns = [
    
    path('',index.as_view(),name="index"),
    path('createTask/',CreateTask.as_view(),name="createTask"),
    path('updateTask/<int:pk>',UpdateTask.as_view(),name="updateTask"),
    path('deleteTask/<int:pk>',DeleteTask.as_view(),name="deleteTask"),
]