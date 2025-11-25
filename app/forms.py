from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    nombres = forms.CharField(min_length=3,max_length=80)
    apellidos = forms.CharField(min_length=4,max_length=80)
    correoElectronico= forms.EmailField(required=True)

    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'profesion', 'correoElectronico']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ''
            
            if field_name == 'correoElectronico':
                field.widget.attrs['placeholder'] = 'tu@email.com'