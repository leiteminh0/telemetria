import csv
import os
import uuid
from decimal import Decimal
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from api_telemetria.models import MedicaoVeiculoTemp, Veiculo, Medicao


def processar_csv_medicoes(arquivo):
    arquivoid = str(uuid.uuid4())
    pasta_destino = os.path.join(settings.MEDIA_ROOT, "importacoes")
    os.makedirs(pasta_destino, exist_ok=True)
    fs = FileSystemStorage(location=pasta_destino)
    filename = fs.save(arquivo.name, arquivo)
    filepath = fs.path(filename)
    resultado = []
    with transaction.atomic():
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                veiculo = Veiculo.objects.get(id=row['veiculo_id'])
                medicao = Medicao.objects.get(id=row['medicao_id'])
                MedicaoVeiculoTemp.objects.create(
                    veiculoid=veiculo,
                    medicaoid=medicao,
                    data=datetime.fromisoformat(row['data']),
                    valor=Decimal(row['valor']),
                    arquivoid=arquivoid
                )
                resultado.append(row)
    return resultado
