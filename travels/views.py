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
    travel = Travel.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'travel': travel
    }
    return render(request, 'travels/index.html', context)

@login_required
def view(request, id):
    travel = Travel.objects.get(id=id)
    context = {
        'travel': travel
    }
    return render(request, 'travels/detail.html', context)

@login_required
def edit(request, id):
    travel = Travel.objects.get(id=id)

    if request.method == 'GET':
        form = TravelForm(instance=travel)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'travels/edit.html', context)
    elif request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
        messages.success(request, 'Viaje actualizado')
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'travels/edit.html', context)

@login_required
def create(request):
    if request.method == "GET":
        form = TravelForm()
        context = {
            'form': form
        }
        return render(request, 'travels/create.html', context)
    elif request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('travel')

class Delete(LoginRequiredMixin, DeleteView):
    model = Travel
    success_url = reverse_lazy('travel') 

