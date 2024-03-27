from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    path('register/', register, name='register'),
    path('perfil/', edit_profile, name='perfil'),
    path('<int:pk>/password/', ChangePassword.as_view(), name='change_password'),
    path('add_avatar/', add_avatar, name='add_avatar'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
    path('delete/<int:user_id>/confirm/', confirm_delete_user, name='confirm_delete_user'),
]
