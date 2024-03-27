from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DeleteView

from .models import *
from .forms import *

@login_required
def index(request,letter=None):
    if letter != None:
        contacts = Contact.objects.filter(last_name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__icontains=request.GET.get('search', ''))
    
    context = {
        'contacts': contacts
    }
    return render(request, 'contact/index.html', context)

@login_required
def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context)

@login_required
def edit(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'GET':
        form = ContactForm(instance = contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'contact/edit.html', context)
    elif request.method == "POST":
        form = ContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado')
        return render(request, 'contact/edit.html', context)

@login_required
def create(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact/create.html', context)

    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')

class Delete(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contact') 

