from rest_framework import serializers
from .models import Evento, Tarea, Contacto, Recordatorio, ArchivoAdjunto, ImagenAdjunta

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = '__all__'

class ArchivoAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoAdjunto
        fields = '__all__'

class ImagenAdjuntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenAdjunta
        fields = '__all__'
