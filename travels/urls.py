from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='travel'),
    path('view/<int:id>', view, name='travel_view'),
    path('edit/<int:id>', edit, name='travel_edit'),
    path('create/', create, name='travel_create'),
    path('delete/<int:pk>', Delete.as_view(), name='travel_delete'),
]

