from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('view_task_line/<str:pk>', views.viewTaskLine, name="view_task_line"),
    path('update_task_line/<str:pk>', views.updateTaskLine, name="update_task_line"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]