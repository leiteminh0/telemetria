"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_telemetria.api.viewsets import *

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'modelos', ModeloViewSet)
router.register(r'unidades-medida', UnidadeMedidaViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'medicoes', MedicaoViewSet)
router.register(r'medicoes-veiculo', MedicaoVeiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
