from django.shortcuts import render,redirect, get_object_or_404
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

def edit(request,id):
    usuario = get_object_or_404(Usuarios, codigo=id)
    data= {
        'form': UsuarioForm(instance=usuario)
    }
    return render(request, 'editarUsuario.html',data)