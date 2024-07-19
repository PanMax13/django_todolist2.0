from django.urls import path
from . import views


patterns = [
    path('<slug:slug>/', views.filter_url, name='category'),
    path('task-data/<int:task_id>/', views.task_menu, name='taskMenu'),
    path('tasks/remove/task_id=<int:task_id>', views.remove_task, name='removeTask'),
    path('tasks/edit/id=<int:task_id>', views.edit, name='editTask'),
    path('tasks/save=<int:task_id>', views.save, name='save'),
    path('tasks/add', views.addTask, name='addTask'),
    path('tasks/saveTask', views.saveTasks, name='saveTask')
]


