from django.db import models

# Create your models here.
class Usuarios(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=80)
    apellidos=models.CharField(max_length=80)
    profesion=models.CharField(max_length=80)
    correoElectronico=models.EmailField(unique=True, null=True)

    #Método que muestra el texto especificado cuando se imprime al objeto
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombres, self.apellidos)
    