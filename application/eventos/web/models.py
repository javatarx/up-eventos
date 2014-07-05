from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos')
    fecha_registro = models.DateTimeField(auto_now=True)

    def __unicode__ (self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(help_text='escribe la descricion del Evento')
    
    def __unicode__ (self):
        return self.nombre
    
class Inscripcion_Email(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    email = models.TextField(help_text='E-mail')
    fecha_registro = models.DateTimeField(auto_now=True)

    
    def __unicode__ (self):
        inscripcion = "%s %s"%(self.nombre,self.email)
        return inscripcion
