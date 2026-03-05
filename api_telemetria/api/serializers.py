from rest_framework import serializers
from api_telemetria.models import (
    Marca,
    Modelo,
    UnidadeMedida,
    Veiculo,
    Medicao,
    MedicaoVeiculo
)
import datetime


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
        extra_kwargs={
            'id': {'help_text': 'Indentificador da Marca'},
            'nome':{'help_text':'Indentificador do nome da marca'}
        }


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        extra_kwargs={
            'id': {'help_text': 'Identificador do Model'},
            'nome': {'help_text': 'Indentificador do nome do modelo'}
        }


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = "__all__"
        extra_kwargs={
           'id': {'help_text': 'Identificador da UnidadeMedida'},
           'nome': {'help_text': 'Indentificador de unidademedida'}  
        }


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        extra_kwargs= {
            'id': {'help_text': 'Identificador único do veículo'}, 
            'descricao': {'help_text': 'Descrição detalhada do veículo'},
            'marca': {'help_text': 'ID da marca do veículo (consulte /api/marcas/)'},
            'modelo': {'help_text': 'ID do modelo do veículo (consulte /api/modelos/)'},
            'ano': {'help_text': 'Ano de fabricação do veículo (1900 até ano atual + 1)'},
            'horimetro': {'help_text': 'Horímetro atual do veículo em horas (deve ser >= 0)'}
        }
    
    def validate_ano(self, value):
        ano_atual = datetime.date.today().year
        if value < 1900 or value > ano_atual + 1:
            raise serializers.ValidationError(
                f"Ano deve estar entre 1900 e {ano_atual + 1}."
            )
        return value
    
    def validate_horimetro(self, value):
        if value < 0:
            raise serializers.ValidationError("Horímetro não pode ser negativo.")
        return value


class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicao
        fields = "__all__"
        extra_kwargs= {
            'id': {'help_text': 'Identificador da Medição'},
            'tipo': {'help_text': 'Indentificador da medicao'},
            'unidade_medida': {'help_text': 'Identificador da medicao. Buscar no Get da Api medicao'},
        }


class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicaoVeiculo
        fields = "__all__"
        extra_kwargs= {
            'id': {'help_text': 'Identificador único da medição do veículo'},
            'veiculo': {'help_text': 'ID do veículo medido (consulte /api/veiculos/)'},
            'medicao': {'help_text': 'ID do tipo de medição (consulte /api/medicoes/)'},
            'data': {'help_text': 'Data e hora em que a medição foi realizada'},
            'valor': {'help_text': 'Valor numérico da medição (deve ser >= 0)'}
        }
    
    def validate_valor(self, value):
        if value < 0:
            raise serializers.ValidationError("Valor da medição não pode ser negativo.")
        return value

