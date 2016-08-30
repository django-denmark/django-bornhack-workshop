from django.shortcuts import render, redirect
from . import models


def task_list(request, **kwargs):
    tasks = models.Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def task_complete(request, **kwargs):
    pk = kwargs.get('pk')
    task = models.Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('task-list')
