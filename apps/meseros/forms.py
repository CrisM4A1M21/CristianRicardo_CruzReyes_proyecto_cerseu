from django.forms import ModelForm
from .models import Meseros


class MeseroForm(ModelForm):
    class Meta:
        model = Meseros
        fields = ('nombre', 'nacionalidad', 'edad', 'procedencia')
