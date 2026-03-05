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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from api_telemetria.api.viewsets import (
    MarcaViewSet,
    ModeloViewSet,
    UnidadeMedidaViewSet,
    VeiculoViewSet,
    MedicaoViewSet,
    MedicaoVeiculoViewSet
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
     openapi.Info(
         title = 'API para telemetria de veiculos agricolas',
         default_version ='v1',
         description = 'Sistema para cadastro e controle por telemetria de frota de veiculos agricolas',
         terms_of_services = 'https://www.google.com/policies/terms/, ese tiver un termo colocar o link',
         contact = openapi.Contact(email='contato@teste.com'),
         license = openapi.License(name= 'OpenSource')
     ),
     public=True,
     permission_classes=[permissions.AllowAny]
)


router = routers.DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'modelos', ModeloViewSet)
router.register(r'unidades-medida', UnidadeMedidaViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'medicoes', MedicaoViewSet)
router.register(r'medicoes-veiculo', MedicaoVeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('swaggerjson/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),]

 