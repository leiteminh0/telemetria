from rest_framework import viewsets
from api_telemetria.api import serializers
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
from drf_yasg.utils import swagger_auto_schema


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de marca",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de marca",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de marca conforme ID informado",
        responses={201: serializers.MarcaSerializer(many=True)}
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera a marca conforme dados passados, para o ID informado",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera parcialmente a marca conforme dados passados, para o ID informado",
        responses={200: serializers.MarcaSerializer()}
    )
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de marca conforme ID informado",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de modelo",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de modelo",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de modelo conforme ID informado",
        responses={201: serializers.ModeloSerializer(many=True)}
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera o modelo conforme dados passados, para o ID informado",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera parcialmente o modelo conforme dados passados, para o ID informado",
        responses={200: serializers.ModeloSerializer()}
    )
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de modelo conforme ID informado",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de unidade de medida",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de unidade de medida",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de unidade de medida conforme ID informado",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de unidade de medida conforme dados passados, para o ID informado",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera parcialmente o tipo de unidade de medida conforme dados passados, para o ID informado",
        responses={200: serializers.UnidadeMedidaSerializer()}
    )
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de unidade de medida conforme ID informado",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de veículo",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de veículo",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de veículo conforme ID informado",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de veículo conforme dados passados, para o ID informado",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera parcialmente o tipo de veículo conforme dados passados, para o ID informado",
        responses={200: serializers.VeiculoSerializer()}
    )
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de veículo conforme ID informado",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    



class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = Medicao.objects.all()
    serializer_class = MedicaoSerializer
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de medição",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de medição conforme ID informado",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição conforme dados passados, para o ID informado",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera parcialmente o tipo de medição conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoSerializer()}
    )
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de medição conforme ID informado",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = MedicaoVeiculo.objects.all()
    serializer_class = MedicaoVeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de medição do veículo",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição do veículo",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de medição do veículo conforme ID informado",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição do veículo conforme dados passados, para o ID informado",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Altera parcialmente o tipo de medição do veículo conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer()}
    )
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de medição do veículo conforme ID informado",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
