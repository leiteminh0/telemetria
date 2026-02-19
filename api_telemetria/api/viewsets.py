from rest_framework import viewsets
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


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = Medicao.objects.all()
    serializer_class = MedicaoSerializer


class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = MedicaoVeiculo.objects.all()
    serializer_class = MedicaoVeiculoSerializer
