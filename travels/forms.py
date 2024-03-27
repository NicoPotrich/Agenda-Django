from django.forms import DateTimeInput, ModelForm
from .models import Travel


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = "__all__"
        widgets = {
            'date_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'estimated_end': DateTimeInput(attrs={'type': 'datetime-local'})
        }
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion / Itinerario',
            'date_time': 'Fecha y hora de salida',
            'estimated_end': 'Fecha y hora de regreso',
        }
