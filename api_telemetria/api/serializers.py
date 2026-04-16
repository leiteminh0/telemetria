from rest_framework import serializers
from api_telemetria.models import Marca, Modelo, UnidadeMedida, Veiculo, Medicao, MedicaoVeiculo, MedicaoVeiculoTemp


class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = '__all__'


class ModeloSerializer(serializers.ModelSerializer):
  class Meta:
    model = Modelo
    fields = '__all__'


class UnidadeMedidaSerializer(serializers.ModelSerializer):
  class Meta:
    model = UnidadeMedida
    fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Veiculo
    fields = '__all__'


class MedicaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Medicao
    fields = '__all__'


class MedicaoVeiculoSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicaoVeiculo
    fields = '__all__'


class MedicaoVeiculoTempSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicaoVeiculoTemp
    fields = '__all__'


# Serializer para upload de CSV
class UploadCSVSerializer(serializers.Serializer):
  arquivo = serializers.FileField()
