from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='contact'),
    path('<letter>', index, name='contact'),
    path('view/<int:id>', view, name='contact_view'),
    path('edit/<int:id>', edit, name='contact_edit'),
    path('create/', create, name='contact_create'),
    path('delete/<int:pk>', Delete.as_view(), name='contact_delete'),
]
