from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DeleteView

from .models import *
from .forms import *

@login_required
def index(request):
    tasks = Task.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'tasks': tasks
    }
    return render(request, 'task/index.html', context)

@login_required
def view(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'task/detail.html', context)

@login_required
def edit(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'GET':
        form = TaskForm(instance=task)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'task/edit.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, 'Tarea actualizada')
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'task/edit.html', context)

@login_required
def create(request):
    if request.method == "GET":
        form = TaskForm()
        context = {
            'form': form
        }
        return render(request, 'task/create.html', context)
    elif request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task')

class Delete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task') 



