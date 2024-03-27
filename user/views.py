from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Intenta obtener la URL del avatar si existe
                try:
                    avatar = Avatar.objects.get(user=user)
                    avatar_url = avatar.image.url
                except Avatar.DoesNotExist:
                    # Si no hay avatar, usa el avatar predeterminado
                    avatar_url = "/media/avatars/default.png"
                    # Crea y guarda el avatar predeterminado
                    avatar = Avatar(user=user, image='avatars/default.png')
                    avatar.save()

                # Establece la URL del avatar en la sesión del usuario
                request.session["avatar"] = avatar_url

                return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            return redirect(reverse_lazy('index'))
    else:
        form = RegistroForm()
        return render(request, 'user/register.html', {'form':form})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=user)

            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")

            user.save()
            return redirect(reverse_lazy('index'))
    else:
        form = UserEditForm(instance=user)
        return render(request, 'user/edit_profile.html', {'form':form})

@login_required
def add_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user

            # Eliminar avatares anteriores del usuario si existen
            Avatar.objects.filter(user=user).delete()

            # Crear un nuevo avatar para el usuario
            avatar = Avatar(user=user, image=form.cleaned_data["image"])
            avatar.save()

            # Actualizar la sesión con la URL del nuevo avatar
            request.session["avatar"] = avatar.image.url

            return redirect('index')
    else:
        form = AvatarForm()
    
    return render(request, 'user/add_avatar.html', {'form': form})

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('perfil')

from django.contrib.auth.decorators import permission_required

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/confirm_delete.html', {'user': user})

@login_required
def confirm_delete_user(request, user_id):
    if request.method == "POST":
        user = User.objects.get(pk=user_id)
        user.delete()
        return redirect('index')
    return redirect('index')

