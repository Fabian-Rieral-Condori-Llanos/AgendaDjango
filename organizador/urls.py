from django.urls import path, include
from .views import (
    EventoViewSet,
    TareaViewSet,
    ContactoViewSet,
    RecordatorioViewSet,
    ArchivoAdjuntoViewSet,
    ImagenAdjuntaViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'tareas', TareaViewSet)
router.register(r'contactos', ContactoViewSet)
router.register(r'recordatorios', RecordatorioViewSet)
router.register(r'archivos-adjuntos', ArchivoAdjuntoViewSet)
router.register(r'imagenes-adjuntas', ImagenAdjuntaViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]

