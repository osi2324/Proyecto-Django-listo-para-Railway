from django import forms
from .models import Equipo
from .models import Perfil


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'input'}),
            'marca': forms.TextInput(attrs={'class':'input'}),
            'estado': forms.Select(attrs={'class':'input'}),
        }
class RolForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['rol']
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-control'})
        }