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
    task = Task.objects.get(id=pk)

    lineItems = task.taskline_set.all()

    context = {'task': task, 'lineItems':lineItems}

    return render(request, 'tasks/view_task_line.html', context)


def updateTaskLine(request, pk):

    line = TaskLine.objects.get(id=pk)
    form = LineForm(instance=line)

    if request.method == 'POST':
        form = LineForm(request.POST, instance=line)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}

    return render(request, 'tasks/update_task_line.html', context)



def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    taskline = task.taskline_set.all()
    
    taskForm = TaskForm(instance=task)

    print(taskForm)

    if request.method == 'POST':
        taskForm = TaskForm(request.POST, instance=task)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('/')
        
    context = {'taskForm':taskForm, 'taskline':taskline}

    return render(request, 'tasks/update_task.html', context )


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        print('request')
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

