from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def viewTaskLine(request, pk):
    print(request, pk)
    task = get_object_or_404(Task, pk=pk)
    taskline = TaskLine.objects.filter(task=task)
    print(taskline)
    return render(request, 'tasks/view_task_line.html', {'task': task, 'taskline': taskline})


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context )

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        print('request')
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

