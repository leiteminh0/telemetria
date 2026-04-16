# Bibliotecas nativas do Python para leitura de CSV, manipulação de arquivos,
# geração de IDs únicos, conversão de números decimais e datas
import csv
import os
import uuid
from decimal import Decimal
from datetime import datetime

# Configurações do Django (MEDIA_ROOT), armazenamento de arquivos e transações de banco
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction, connection

# Models necessários para persistência dos dados importados
from api_telemetria.models import MedicaoVeiculoTemp, Veiculo, Medicao


def executar_procedure_pos_importacao(arquivoid):
    # Abre uma conexão direta com o banco e executa uma stored procedure MySQL
    # passando o arquivoid como parâmetro para processar os dados importados
    with connection.cursor() as cursor:
        cursor.callproc("processa_arquivo", [arquivoid])


def processar_csv_medicoes(arquivo):
    # Gera um ID único (UUID) para identificar este lote de importação
    # Cada arquivo enviado recebe um arquivoid diferente
    arquivoid = str(uuid.uuid4())

    # Define a pasta de destino dentro de media/ e cria se não existir
    pasta_destino = os.path.join(settings.MEDIA_ROOT, "importacoes_medicao")
    os.makedirs(pasta_destino, exist_ok=True)

    # Salva o arquivo físico no servidor com o UUID no nome para evitar conflitos
    nome_salvo = f"{arquivoid}_{arquivo.name}"
    fs = FileSystemStorage(location=pasta_destino)
    nome_arquivo_salvo = fs.save(nome_salvo, arquivo)
    caminho_completo = os.path.join(pasta_destino, nome_arquivo_salvo)

    # Inicializa contadores e listas para controle do processamento
    total_linhas_arquivo = 0
    erros = []
    linhas_para_inserir = []

    # Carrega todos os veículos e medições do banco em memória (cache)
    # Evita fazer uma query por linha do CSV — muito mais performático
    veiculos_cache = {v.id: v for v in Veiculo.objects.all()}
    medicoes_cache = {m.id: m for m in Medicao.objects.all()}

    # Abre o arquivo CSV salvo para leitura
    with open(caminho_completo, mode="r", encoding="utf-8-sig", newline="") as f:
        # DictReader lê cada linha como dicionário usando o cabeçalho como chave
        # delimiter=';' indica que o CSV usa ponto e vírgula como separador
        reader = csv.DictReader(f, delimiter=';')

        # Define quais colunas são obrigatórias no cabeçalho do CSV
        campos_esperados = {"veiculoid", "medicaoid", "data", "valor"}

        # Valida se o CSV tem cabeçalho
        if not reader.fieldnames:
            raise Exception("O CSV não possui cabeçalho.")

        # Valida se todas as colunas esperadas estão presentes no cabeçalho
        if not campos_esperados.issubset(set(reader.fieldnames)):
            raise Exception(
                f"Cabeçalho inválido. Esperado: {list(campos_esperados)}. Recebido: {reader.fieldnames}"
            )

        # Percorre cada linha do CSV (start=2 porque linha 1 é o cabeçalho)
        for numero_linha, row in enumerate(reader, start=2):
            total_linhas_arquivo += 1

            try:
                # Converte os IDs de string para inteiro
                id_veiculo = int(row["veiculoid"])
                id_medicao = int(row["medicaoid"])

                # Busca o veículo no cache em vez de consultar o banco
                veiculo = veiculos_cache.get(id_veiculo)
                if not veiculo:
                    raise Exception(f"Veículo {id_veiculo} não encontrado.")

                # Busca a medição no cache em vez de consultar o banco
                medicao = medicoes_cache.get(id_medicao)
                if not medicao:
                    raise Exception(f"Medição {id_medicao} não encontrada.")

                # Converte a string de data para objeto datetime no formato esperado
                data_convertida = datetime.strptime(
                    row["data"].strip(),
                    "%Y-%m-%d %H:%M:%S"
                )

                # Converte o valor string para Decimal (precisão para valores numéricos)
                valor_convertido = Decimal(row["valor"].strip())

                # Monta o objeto MedicaoVeiculoTemp sem salvar ainda no banco
                linhas_para_inserir.append(
                    MedicaoVeiculoTemp(
                        veiculoid=veiculo,
                        medicaoid=medicao,
                        data=data_convertida,
                        valor=valor_convertido,
                        arquivoid=arquivoid
                    )
                )

            except Exception as e:
                # Registra o erro da linha sem interromper o processamento das demais
                erros.append({
                    "linha": numero_linha,
                    "erro": str(e)
                })

    total_linhas_validas = len(linhas_para_inserir)

    # Bloco atômico: ou tudo é salvo, ou nada é salvo (rollback automático em caso de erro)
    with transaction.atomic():
        if linhas_para_inserir:
            # bulk_create insere todas as linhas de uma vez em vez de um INSERT por linha
            # batch_size=1000 divide em lotes de 1000 para não sobrecarregar o banco
            MedicaoVeiculoTemp.objects.bulk_create(linhas_para_inserir, batch_size=1000)

        # Verifica se a quantidade de linhas válidas bate com o esperado
        quantidades_conferem = total_linhas_validas == 9

        if quantidades_conferem:
            # Se tudo conferir, executa a stored procedure para processar os dados
            executar_procedure_pos_importacao(arquivoid)
        else:
            # Se houver divergência, desfaz a importação deletando os registros do lote
            MedicaoVeiculoTemp.objects.filter(arquivoid=arquivoid).delete()

    # Retorna um resumo completo da importação para o endpoint exibir na resposta
    return {
        "arquivoid": arquivoid,
        "arquivo_salvo": nome_arquivo_salvo,
        "caminho": caminho_completo,
        "total_linhas_arquivo": total_linhas_arquivo,
        "total_linhas_importadas": 9,
        "quantidades_conferem": total_linhas_arquivo == 9,
        "erros": erros
    }
