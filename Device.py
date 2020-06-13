from paho.mqtt.client import Client
from config import *


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def on_publish(client: Client, userdata, mid):
    pass
    # print(client._client_id)


def on_disconnect(client, userdata, rc):
    print("return result is " + str(rc))


class Device(Client):
    def __init__(self, id):
        super().__init__(client_id=id)
        self.on_connect = on_connect
        self.on_message = on_message
        self.on_publish = on_publish
        self.on_disconnect = on_disconnect

    def start(self):
        self.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
        self.loop_start()
        # self.subscribe("/basic/+")

    def finish(self):
        self.loop_stop()
        self.disconnect()



