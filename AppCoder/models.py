from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Viaje(models.Model):
    
    def __str__(self):
        
        return f"Lugar: {self.nombre} --- Duración: {self.duracion}"
    
    nombre = models.CharField(max_length=30)
    duracion = models.IntegerField()
    
class Libro(models.Model):
    
    def __str__(self):
        
        return f"Lugar: {self.nombre} --- Autor: {self.autor}"
    
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=30)
    
class Actividad(models.Model):
    
    def __str__(self):
        
        return f"Nombre: {self.nombre} --- Frecuencia: {self.frecuencia}"
    nombre = models.CharField(max_length=40)
    frecuencia = models.IntegerField()
    
class Curso(models.Model):
    
    def __str__(self):
        
        return f"Nombre: {self.nombre} --- docente: {self.docente}"
    
    nombre = models.CharField(max_length=50)
    docente = models.CharField(max_length=30)

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
       