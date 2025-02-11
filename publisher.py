import paho.mqtt.client as paho

broker = ""
port = 1883
topic = ""

client = paho.Client()
client.connect(broker, port)

while True:
    mensagem = input(f"Digite uma mensagem para ser enviada ao tópico '{topic}'")
    client.publish(topic, mensagem)
    print("Mensagem enviada.\n")