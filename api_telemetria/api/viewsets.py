from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from api_telemetria.api.mixins import SwaggerDocMixin
from api_telemetria.api import serializers
from api_telemetria.api.services import processar_csv_medicoes
from api_telemetria import models
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


class ImportarMedicaoCSVViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UploadCSVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        arquivo = serializer.validated_data["arquivo"]
        try:
            resultado = processar_csv_medicoes(arquivo)
            return Response(
                {"mensagem": "Arquivo processado com sucesso.", "resultado": resultado},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"erro": "Falha ao processar o arquivo.", "detalhe": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class MedicaoVeiculoTempViewsets(SwaggerDocMixin, viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoVeiculoTempSerializer
    queryset = models.MedicaoVeiculoTemp.objects.all()
