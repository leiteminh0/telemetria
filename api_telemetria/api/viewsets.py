from rest_framework import viewsets
from api_telemetria.api.mixins import SwaggerDocMixin
from api_telemetria.models import (
    Marca,
    Modelo,
    UnidadeMedida,
    Veiculo,
    Medicao,
    MedicaoVeiculo
)
from api_telemetria.api.serializers import (
    MarcaSerializer,
    ModeloSerializer,
    UnidadeMedidaSerializer,
    VeiculoSerializer,
    MedicaoSerializer,
    MedicaoVeiculoSerializer
)


class MarcaViewSet(SwaggerDocMixin, viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ModeloViewSet(SwaggerDocMixin, viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


class UnidadeMedidaViewSet(SwaggerDocMixin, viewsets.ModelViewSet):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer


class VeiculoViewSet(SwaggerDocMixin, viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class MedicaoViewSet(SwaggerDocMixin, viewsets.ModelViewSet):
    queryset = Medicao.objects.all()
    serializer_class = MedicaoSerializer


class MedicaoVeiculoViewSet(SwaggerDocMixin, viewsets.ModelViewSet):
    queryset = MedicaoVeiculo.objects.all()
    serializer_class = MedicaoVeiculoSerializer
