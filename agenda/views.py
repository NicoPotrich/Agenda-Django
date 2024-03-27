from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html', {})

def about_me(request):
    return render(request, 'about_me.html', {})

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('perfil')
