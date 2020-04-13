# from django.shortcuts import render
from mto_catalogo import models
from mto_catalogo import serializers, filters
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class SituacionesViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar situaciones.
    """
    queryset = models.Situacion.objects.all()#.order_by('-date_joined')
    serializer_class = serializers.SituacionSerializer

class EstilosViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar estilos.
    """
    queryset = models.Estilo.objects.all()#.order_by('-date_joined')
    serializer_class = serializers.EstiloSerializer

class UsosViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar usos.
    """
    queryset = models.UsoActual.objects.all()#.order_by('-date_joined')
    serializer_class = serializers.UsoActualSerializer

class RiesgosViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar riesgos.
    """
    queryset = models.Riesgo.objects.all().order_by('orden')
    serializer_class = serializers.RiesgoSerializer

class EstadosConservacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar estados de conservación.
    """
    queryset = models.EstadoConservacion.objects.all().order_by('orden')
    serializer_class = serializers.EstadoConservacionSerializer

class ZonasViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar zonas. 
    """
    queryset = models.Zona.objects.all()
    serializer_class = serializers.ZonaSerializer

class SubzonasViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar subzonas. 
    """
    queryset = models.Subzona.objects.all()
    serializer_class = serializers.SubzonaSerializer

class TipologiasViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar tipologías. 
    """
    queryset = models.Tipologia.objects.all()
    serializer_class = serializers.TipologiaSerializer

class SubtipologiasViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite consultar subtipologías. 
    """
    queryset = models.Subtipologia.objects.all()
    serializer_class = serializers.SubtipologiaSerializer


class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = { 
        'default': None,
    }

    def get_serializer_class(self):
            return self.serializers.get(self.action,
                        self.serializers['default'])

class ElementoPatrimonioViewSet(MultiSerializerViewSet):
    """
    API endpoint que permite consultar un elemento individualmente. 
    """
    queryset = models.ElementoPatrimonio.objects.all()
    # serializer_class = serializers.ElementoPatrimonioSerializer
    serializers = {
        'default': serializers.ElementoPatrimonioSerializer,
        'list':    serializers.ElementoPatrimonioListadoSerializer,
        'retrieve':  serializers.ElementoPatrimonioSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ElementoPatrimonioFilter

    def get_serializer_class(self):
        return self.serializers.get(self.action,
            self.serializers['default'])
