import os
import json
import datetime
import django
import paho.mqtt.client as mqtt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from django.conf import settings
from django.utils import timezone
from api_telemetria.models import MedicaoVeiculo, Veiculo, Medicao


def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado com rc={rc}")
    topic = settings.MQTT.get("TOPIC", "dadosSensor")
    client.subscribe(topic)
    print(f"[MQTT] Inscrito em {topic}")


def inserir_medicao(item):
    """Processa e insere um único registro de medição no banco de dados."""

    # Valida se todos os campos obrigatórios estão presentes no payload
    campos = ['valor', 'veiculoid', 'sensorid', 'data']
    if not all(k in item for k in campos):
        raise ValueError(f"Payload incompleto. Esperado: {campos}. Recebido: {list(item.keys())}")

    valor = float(item["valor"])
    veiculoid = int(item["veiculoid"])
    medicaoid = int(item["sensorid"])

    # Converte a string de data para datetime com timezone (USE_TZ=True no settings)
    datae = timezone.make_aware(
        datetime.datetime.fromisoformat(item["data"])
    )

    # Busca com mensagem de erro descritiva para facilitar diagnóstico
    veiculo = Veiculo.objects.filter(id=veiculoid).first()
    if not veiculo:
        raise ValueError(f"Veículo id={veiculoid} não encontrado no banco.")

    medicao = Medicao.objects.filter(id=medicaoid).first()
    if not medicao:
        raise ValueError(f"Medição id={medicaoid} não encontrada no banco.")

    MedicaoVeiculo.objects.create(
        data=datae,
        veiculo=veiculo,
        medicao=medicao,
        valor=valor,
    )

    print(f"[MQTT] Salvo: veiculo={veiculoid} medicao={medicaoid} valor={valor}")


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        # Percorre o vetor e chama a função de inserção para cada item
        for item in data:
            inserir_medicao(item)

    except Exception as e:
        print(f"[ERRO] Falha ao processar mensagem: {e}")


def main():
    mqtt_cfg = settings.MQTT

    host = mqtt_cfg.get("HOST", "127.0.0.1")
    port = mqtt_cfg.get("PORT", 1883)
    keepalive = mqtt_cfg.get("KEEPALIVE", 60)
    client_id = mqtt_cfg.get("CLIENT_ID", "django-mqtt-worker")
    user = mqtt_cfg.get("USERNAME")
    password = mqtt_cfg.get("PASSWORD")

    client = mqtt.Client(client_id=client_id)

    if user and password:
        client.username_pw_set(user, password)

    client.on_connect = on_connect
    client.on_message = on_message

    print(f"[MQTT] Conectando em {host}:{port}...")
    client.connect(host, port, keepalive)

    client.loop_forever()


if __name__ == "__main__":
    main()
