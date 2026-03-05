from rest_framework import serializers
from api_telemetria.models import (
    Marca,
    Modelo,
    UnidadeMedida,
    Veiculo,
    Medicao,
    MedicaoVeiculo
)


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
            'id': {'help_text': 'Identificador do Veiculo'}, 
            'descricao': {'help_text': 'Indentificador do veiculo'},
            'marca': {'help_text': 'Indentificador do veiculo. Buscar no Get da Api veiculo'},
            'modelo': {'help_text': 'Indentificador do veiculo.Buscar no Get da Api veiculo'},
            'ano': {'help_text': 'Ano de fabricacao do veiculo'},
            'horimetro': {'help_text': 'Horimetro rodado por kilometro do veiculo'}
        }


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
            'id': {'help_text': 'Identificador da Medição veiculo'},
            'veiculoid': {'help_text': 'Identificador do veiculo. Buscar no Get da Api veiculo'},
            'medicaoid': {'help_text': 'Identificador do tipo de medição. Buscar no Get da API Medicao'},
            'data': {'help_text': 'Data e hora da medição realizada, essa informação deve vir da automação'},
            'valor': {'help_text': 'Valor medido na automação.'}

          }

