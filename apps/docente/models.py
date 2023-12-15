from django.db import models

# Create your models here.

class TituloDocenteModel(models.Model):
    nombre_corto = models.CharField(max_length=15)
    nombre_completo = models.CharField(max_length=200)
    titulo_docente = models.BooleanField(defautl=True)
    numero_registro = models.CharField(max_length=15)
    fecha = models.CharField(verbose_name='Año', max_length=5)
    

class DocenteModel(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=250)
    localidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email= models.EmailField(max_length=200, unique=True)
    


    
  

