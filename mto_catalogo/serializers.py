from rest_framework import serializers
from mto_catalogo.models import ElementoPatrimonio, EstadoConservacion, Estilo, Historia, Riesgo, Situacion, Subtipologia, Subzona, Tipologia, UsoActual, Zona

class SituacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Situacion
        fields = ('id', 'nombre')

class EstiloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estilo
        fields = ('id', 'nombre')

class UsoActualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsoActual
        fields = ('id', 'nombre')

class EstadoConservacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstadoConservacion
        fields = ('id', 'nombre', 'orden')

class RiesgoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Riesgo
        fields = ('id', 'nombre', 'orden')

class SubzonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subzona
        fields = ('id', 'zona_id', 'codigo', 'nombre')

class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    # subzonas = SubzonaSerializer(many=True)

    class Meta:
        model = Zona
        fields = ('id', 'codigo', 'nombre')
    
class SubtipologiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subtipologia
        fields = ('id', 'tipologia_id', 'nombre')

class TipologiaSerializer(serializers.HyperlinkedModelSerializer):
    # subtipologias = SubtipologiaSerializer(many=True)

    class Meta:
        model = Tipologia
        fields = ('id', 'nombre')

class HistoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Historia
        fields = ('id', 'elemento_id', 'actuacion', 'datacion', 'autor', 'estilo_id')

class ElementoPatrimonioSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para un elemento de patrimonio individual
    """
    historia = HistoriaSerializer(many=True)

    class Meta:
        model = ElementoPatrimonio
        fields = ('id', 'codigo', 'denominacion', 'alturas', 'zona_id', 'subzona_id', 'historia')

class ElementoPatrimonioListadoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para un elemento de patrimonio dentro de un listado
    """
    zona_codigo = serializers.CharField(source='zona.codigo', read_only=True)
    subzona_codigo = serializers.CharField(source='subzona.codigo', read_only=True)

    class Meta:
        model = ElementoPatrimonio
        exclude = ['numero', 'zona', 'subzona', 'tipologia', 'subtipologia', 'situacion',
            'uso_actual', 'estado_conservacion', 'riesgo']
