from django.contrib import admin
from .models import Evento, Tarea, Contacto, Recordatorio, ArchivoAdjunto, ImagenAdjunta

# Register your models here.

admin.site.register(Evento)
admin.site.register(Tarea)
admin.site.register(Contacto)
admin.site.register(Recordatorio)
admin.site.register(ArchivoAdjunto)
admin.site.register(ImagenAdjunta)