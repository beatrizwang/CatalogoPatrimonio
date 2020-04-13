from django_filters import rest_framework as filters
from mto_catalogo import models
from django.db.models import Q

class ElementoPatrimonioFilter(filters.FilterSet):
    denominacion = filters.CharFilter(method='filtrar_denominacion')
    via = filters.CharFilter('direccion', lookup_expr='contains')
    zona = filters.ModelChoiceFilter('zona_id', queryset=models.Zona.objects.all())
    subzona = filters.ModelChoiceFilter('subzona_id', queryset=models.Subzona.objects.all())
    tipologia = filters.ModelChoiceFilter('tipologia_id', queryset=models.Tipologia.objects.all())
    subtipologia = filters.ModelChoiceFilter('subtipologia_id', queryset=models.Subtipologia.objects.all())
    
    exento = filters.BooleanFilter(method='filtrar_exento')

    alturas = filters.NumberFilter('alturas')
    uso_actual = filters.ModelChoiceFilter('uso_actual_id', queryset=models.UsoActual.objects.all())
    estado_conservacion = filters.ModelChoiceFilter('estado_conservacion_id', queryset=models.EstadoConservacion.objects.all())
    riesgo = filters.ModelChoiceFilter('riesgo_id', queryset=models.Riesgo.objects.all())

    def filtrar_denominacion(self, queryset, name, value):
        return queryset.filter(Q(denominacion__contains=value) | Q(denominacion_alt__contains=value))

    def filtrar_exento(self, queryset, name, value):
        if (value):
            return queryset.filter(situacion_id=1)
        return queryset.filter(situacion_id=2)
