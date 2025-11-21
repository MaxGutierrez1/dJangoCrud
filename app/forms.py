from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'profesion', 'correoElectronico']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full border'
            
            if field_name == 'correoElectronico':
                field.widget.attrs['placeholder'] = 'tu@email.com'