"""catalogopatrimonio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from mto_catalogo import views

router = routers.DefaultRouter()
router.register(r'situaciones', views.SituacionesViewSet)
router.register(r'estilos', views.EstilosViewSet)
router.register(r'usos', views.UsosViewSet)
router.register(r'riesgos', views.RiesgosViewSet)
router.register(r'estadosconservacion', views.EstadosConservacionViewSet)
router.register(r'zonas', views.ZonasViewSet)
router.register(r'subzonas', views.SubzonasViewSet)
router.register(r'tipologias', views.TipologiasViewSet)
router.register(r'subtipologias', views.SubtipologiasViewSet)
router.register(r'elementos', views.ElementoPatrimonioViewSet)
# router.register(r'elementos/<int:pk>', views.ElementoPatrimonioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
