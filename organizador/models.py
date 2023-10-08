from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

def validate_future_date(value):
    if value <= timezone.now().date():
        raise ValidationError("La fecha debe ser en el futuro.")

# Función de validación personalizada para el número de teléfono
def validate_phone_number(value): 
    if not value.isdigit() or len(value) != 12:
        raise ValidationError("El número de teléfono debe tener 10 dígitos numéricos.")
    
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(validators=[validate_future_date])
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_limite = models.DateField(validators=[validate_future_date])
    completada = models.BooleanField(default=False)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, validators=[validate_phone_number])

class Recordatorio(models.Model):
    contenido = models.TextField()
    fecha_recordatorio = models.DateTimeField(validators=[validate_future_date])

class ArchivoAdjunto(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='archivos_adjuntos/')

class ImagenAdjunta(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_adjuntas/')

