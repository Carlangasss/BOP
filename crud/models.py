from django.db import models

# Create your models here.

class Dispositivo(models.Model):
    titulo = models.CharField(max_length=200, null=False, unique=True, verbose_name= "Nombre Dispositivo")
    cordenadaX = models.CharField(max_length=100)
    cordenadaY = models.CharField(max_length=100)
    consumoHora = models.CharField(max_length=100, verbose_name= "Consumo por hora")

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    nombreUsuario = models.CharField(verbose_name= "Nombre Usuario", max_length=100 ,null=False, unique=False)
    correoElectronico = models.EmailField(verbose_name= "Correo Electrónico",max_length=50, unique=True)
    contraseña = models.CharField(verbose_name= "Contraseña", max_length=20, unique=True, null= False)

    def __str__(self):
        return self.nombreUsuario
    
class Comuna(models.Model):
    idComuna = models.CharField(primary_key=True, unique=True,verbose_name="ID",max_length=30)
    nombreComuna = models.CharField(max_length=200, null=False, verbose_name="Comuna")
    
    def __str__(self):
        return self.nombreComuna
    
class Provincia(models.Model):
    idProvincia = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombreProvincia = models.CharField(max_length=200, null=False, verbose_name="Provincia")

    def __str__(self):
        return self.nombreProvincia
    
class Region(models.Model):
    idRegion = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombreRegion = models.CharField(max_length=200, null=False, verbose_name="Región")

    def __str__(self):
        return self.nombreRegion
    
class Propiedad(models.Model):
    idPropiedad = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombrePropiedad = models.CharField(max_length=200, null=False, verbose_name="Nombre de la Propiedad")
    direccionPropiedad = models.CharField(max_length=200, null=False, verbose_name="Dirección")

    def __str__(self):
        return self.nombrePropiedad

class Sectores(models.Model):
    idSector = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombreSector = models.CharField(max_length=200, null=False, verbose_name="Nombre del Sector")
    metrosCuadrados = models.FloatField(max_length=15, verbose_name="Metros^2")

    def __str__(self):
        return self.nombreSector
    
class TipoSector(models.Model):
    idSector = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    tipoSector = models.CharField(max_length=200, null=False, verbose_name="Tipo Sector")

    def __str__(self):
        return self.tipoSector
