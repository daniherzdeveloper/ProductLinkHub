"""
URL configuration for ProductLinkHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MejorRelacionCalidadPrecio.as_view(), name="index"),
    path('mejor-relacion-calidad-precio-mas-vendidos/<int:pk>', MejorRelacionCalidadPrecio.as_view(), name="mejor_relacion_calidad_precio"),
    path('los-mas-vendidos-generales/<int:pk>', MasVendidosGenerales.as_view(), name="mas_vendidos_generales"),
    path('imagen-fondo/', imagenfondo, name="imagen_fondo"),
    path('ofertas-especiales/<int:pk>', OfertasEspeciales.as_view(), name="ofertas_especiales"),
] + static(settings.MEDIA_URL, document_root=settings.BASE_DIR)
