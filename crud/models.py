from django.db import models

# Create your models here.

class Dispositivo(models.Model):
    nombreDisp = models.CharField(max_length=200, null=False, unique=True, verbose_name= "Nombre Dispositivo")
    cordenadaX = models.CharField(max_length=100)
    cordenadaY = models.CharField(max_length=100)
    consumoHora = models.CharField(max_length=100, verbose_name= "Consumo por hora")
    fecha = models.DateTimeField(max_length=50,verbose_name="Fecha")

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    nombreUsuario = models.CharField(verbose_name= "Nombre Usuario", max_length=100 ,null=False, unique=False)
    correoElectronico = models.EmailField(verbose_name= "Correo Electrónico",max_length=50, unique=True)
    contraseña = models.CharField(verbose_name= "Contraseña", max_length=20, unique=True, null= False)

    def __str__(self):
        return self.nombreUsuario