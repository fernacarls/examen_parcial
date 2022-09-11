from django.db import models
import datetime

# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo_usuario = models.CharField(max_length=128,default='')
    psw_usuario = models.CharField(max_length=128,default='')

class tareas (models.Model):
    descripcion = models.CharField(max_length=128,default='0')
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_entrega = models.DateField(default=datetime.date.today)
    usuario_responsable = models.CharField(max_length=128,default='0')
    estado_tarea = models.CharField(max_length=128,default='Programada')