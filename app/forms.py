from django import forms
from .models import Usuarios
class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields=['nombres','apellidos','profesion','correoElectronico']

        #widgets
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs) # Inicializa el formulario primero
                
                for field_name, field in self.fields.items():
                    field.widget.attrs['class'] = 'w-full border'
                    
                    if field_name == 'email':
                        field.widget.attrs['placeholder'] = 'tu@email.com'