import paho.mqtt.client as paho

broker = ""
port = 1883
topic = ""

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

client = paho.Client()
client.on_message = on_message
client.connect(broker, port)

client.subscribe(topic)
print(f"Inscrito no tópico {topic}")

client.loop_forever()