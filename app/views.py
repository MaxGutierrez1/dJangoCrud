from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from .forms import UsuarioForm
# Create your views here.

def home(request):
    usuarios = Usuarios.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios": usuarios})

def register(request):
    data={
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario= UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Usuario guardado"
        else:
            data["form"] = formulario
    return render(request, "registroUsuarios.html",data)

 