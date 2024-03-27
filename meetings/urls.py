from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='meetings'),
    path('view/<int:id>', view, name='meeting_view'),
    path('edit/<int:id>', edit, name='meeting_edit'),
    path('create/', create, name='meeting_create'),
    path('delete/<int:pk>', Delete.as_view(), name='meeting_delete'),
]

