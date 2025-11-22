from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('registro/',views.register, name="registrar_usuario"),
    path('editar/<id>/', views.edit, name="editar_usuario"),
    path('eliminar/<id>', views.delete,name="eliminar_usuario"),
]