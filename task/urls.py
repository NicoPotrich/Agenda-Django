from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='task'),
    path('view/<int:id>', view, name='task_view'),
    path('edit/<int:id>', edit, name='task_edit'),
    path('create/', create, name='task_create'),
    path('delete/<int:pk>', Delete.as_view(), name='task_delete'),
]
