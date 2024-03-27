from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'mobile': 'Móvil',
            'phone': 'Teléfono',
            'email': 'Correo electrónico',
            'company': 'Empresa',
            'date': 'Fecha',
            'notes': 'Notas',
        }