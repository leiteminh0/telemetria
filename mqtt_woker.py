import os
import json
import datetime
import django
import paho.mqtt.client as mqtt
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from django.conf import settings
from api_telemetria.models import MedicaoVeiculo, Veiculo, Medicao


def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado com rc={rc}")
    topic = settings.MQTT.get("TOPIC", "dadosSensor")
    client.subscribe(topic)
    print(f"[MQTT] Inscrito em {topic}")


def inserir_medicao(item):
    """Processa e insere um único registro de medição no banco de dados."""
    valor = float(item["valor"])
    veiculoid = int(item["veiculoid"])
    medicaoid = int(item["sensorid"])
    datae = datetime.datetime.fromisoformat(item["data"])

    veiculo = Veiculo.objects.get(id=veiculoid)
    medicao = Medicao.objects.get(id=medicaoid)

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
    user = mqtt_cfg.get("USERNAME")
    password = mqtt_cfg.get("PASSWORD")

    client = mqtt.Client()

    if user and password:
        client.username_pw_set(user, password)

    client.on_connect = on_connect
    client.on_message = on_message

    print(f"[MQTT] Conectando em {host}:{port}…")
    client.connect(host, port, 60)

    client.loop_forever()


if __name__ == "__main__":
    main()