from django.shortcuts import render
from rest_framework import viewsets, generics

# Create your views here.

from .models import Evento, Tarea, Contacto, Recordatorio, ArchivoAdjunto, ImagenAdjunta
from .serializers import EventoSerializer, TareaSerializer, ContactoSerializer, RecordatorioSerializer, ArchivoAdjuntoSerializer, ImagenAdjuntaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer

class ArchivoAdjuntoViewSet(viewsets.ModelViewSet):
    queryset = ArchivoAdjunto.objects.all()
    serializer_class = ArchivoAdjuntoSerializer

class ImagenAdjuntaViewSet(viewsets.ModelViewSet):
    queryset = ImagenAdjunta.objects.all()
    serializer_class = ImagenAdjuntaSerializer