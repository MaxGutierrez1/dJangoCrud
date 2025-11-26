from django.shortcuts import render,redirect, get_object_or_404
from .models import Usuarios
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
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
    nombre= usuario.nombres
    data= {
        'form': UsuarioForm(instance=usuario),
        'nombre' : nombre
    }
    if request.method =='POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado")
            data["mensaje"] = "Usuario actualizado"
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'editarUsuario.html',data)

def delete(request,id):
    usuario=get_object_or_404(Usuarios, codigo=id)
    usuario.delete()
    messages.success(request, "Eliminado")
    return redirect(to="home")
