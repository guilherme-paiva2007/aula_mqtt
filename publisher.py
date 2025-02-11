import paho.mqtt.client as paho

broker = "broker.hivemq.com"
port = 1883
topic = "senai/dev"

client = paho.Client()
client.connect(broker, port)

while True:
    mensagem = input(f"Digite uma mensagem para ser enviada ao tópico '{topic}'")
    client.publish(topic, mensagem)
    print("Mensagem enviada.\n")