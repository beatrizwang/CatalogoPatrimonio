from django.db import models

class ElementoPatrimonio(models.Model):

    id = models.AutoField(primary_key=True)

    # Datos básicos
    codigo = models.CharField(max_length=5, db_index=True, editable=False, null=True)
    numero = models.IntegerField(editable=False, null=True)
    denominacion = models.CharField(max_length=255, null=True)
    denominacion_alt = models.CharField(max_length=2000, null=True, blank=True)

    # Localización
    direccion = models.CharField(max_length=2000, null=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True)
    zona = models.ForeignKey('Zona', on_delete=models.PROTECT, null=True)
    subzona = models.ForeignKey('Subzona', on_delete=models.PROTECT, null=True)

    # Caracterización
    tipologia = models.ForeignKey('Tipologia', on_delete=models.PROTECT, null=True, blank=True)
    subtipologia = models.ForeignKey('Subtipologia', on_delete=models.PROTECT, null=True, blank=True)
    situacion = models.ForeignKey('Situacion', on_delete=models.PROTECT, null=True)
    alturas = models.SmallIntegerField(default=0, null=True)

    # Estado
    desaparecido = models.BooleanField(default=False)
    uso_actual = models.ForeignKey('UsoActual', on_delete=models.PROTECT, null=True, blank=True)
    estado_conservacion = models.ForeignKey('EstadoConservacion', on_delete=models.PROTECT, null=True)
    riesgo = models.ForeignKey('Riesgo', on_delete=models.PROTECT, null=True, blank=True)
    
    # Otros
    observaciones = models.CharField(max_length=2000, null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    # protecciones = models.ManyToManyField('Proteccion',
    #     through='ElementoProteccion',
    #     through_fields=('elemento', 'proteccion'))

    class Meta: 
        # ordering = ["-my_field_name"]
        db_table = 'CAT_ElementosPatrimonio'

    # Métodos
    # def get_absolute_url(self):
    #     """
    #     Devuelve la url para acceder a una instancia particular de MyModelName.
    #     """
    #     return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.denominacion


# Tablas satélite

# class Proteccion(models.Model):
    
#     id = models.AutoField(primary_key=True)
#     marco_proteccion = models.CharField(max_length=255, null=True)
#     grado_proteccion = models.CharField(max_length=255, null=True)
#     ano = models.IntegerField(null=True)
#     anulado = models.BooleanField(default=False)

#     elementos = models.ManyToManyField(ElementoPatrimonio,
#         through='ElementoProteccion',
#         through_fields=('proteccion', 'elemento'))

#     class Meta:
#         db_table = 'CAT_Protecciones'

#     def __str__(self):
#         return self.marco_proteccion


# class ElementoProteccion(models.Model):

#     id = models.AutoField(primary_key=True)
#     elemento = models.ForeignKey('ElementoPatrimonio', on_delete=models.CASCADE)
#     proteccion = models.ForeignKey('Proteccion', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'CAT_ElementosProtecciones'


class Historia(models.Model):
    
    id = models.AutoField(primary_key=True)
    elemento = models.ForeignKey('ElementoPatrimonio', related_name='historia', on_delete=models.CASCADE)
    actuacion = models.CharField(max_length=255, null=True)
    datacion = models.CharField(max_length=255, null=True, blank=True)
    autor = models.CharField(max_length=255, null=True, blank=True)
    estilo = models.ForeignKey('Estilo', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = 'CAT_Historia'

    def __str__(self):
        return self.actuacion


# Modelos para datos maestros

class DatoMaestro(models.Model):
    """
    Clase abstracta para datos maestros con id y Nombre(60)
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

class DatoMaestroOrdenado(DatoMaestro):
    """
    Clase abstracta para datos maestros con id, nombre(60) y orden
    """
    orden = models.SmallIntegerField(default=0, null=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Zona(DatoMaestro):

    codigo = models.CharField(max_length=1)

    class Meta:
        db_table = 'CAT_Zonas'


class Subzona(DatoMaestro):

    zona = models.ForeignKey('Zona', related_name='subzonas', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=1)
    
    class Meta:
        db_table = 'CAT_Subzonas'


class Tipologia(DatoMaestro):
    
    class Meta:
        db_table = 'CAT_Tipologias'


class Subtipologia(DatoMaestro):
    
    tipologia = models.ForeignKey('Tipologia', related_name='subtipologias', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'CAT_Subtipologias'


class Situacion(DatoMaestro):
    
    class Meta:
        db_table = 'CAT_Situaciones'


class UsoActual(DatoMaestro):
    
    class Meta:
        db_table = 'CAT_UsosActuales'


class Estilo(DatoMaestro):

    class Meta:
        db_table = 'CAT_Estilos'


class EstadoConservacion(DatoMaestroOrdenado):
    
    class Meta:
        db_table = 'CAT_EstadosConservacion'


class Riesgo(DatoMaestroOrdenado):
    
    class Meta:
        db_table = 'CAT_Riesgos'

