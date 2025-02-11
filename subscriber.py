import paho.mqtt.client as paho

broker = "broker.hivemq.com"
port = 1883
topic = "senai/dev"

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

client = paho.Client()
client.on_message = on_message
client.connect(broker, port)

client.subscribe(topic)
print(f"Inscrito no tópico {topic}")

client.loop_forever()