from paho.mqtt.client import Client
from config import *
import json
# from zbxsend import Metric, send_to_zabbix


class MQTTAgent:
    def __init__(self):
        pass

    def process_data(self, topic, value):
        # send_to_zabbix(("MQTT_AGENT", topic, value), ZABBIX_HOST, ZABBIX_PORT)
        pass

agent_obj = MQTTAgent()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    agent_obj.process_data(msg.topic, str(msg.payload))


def on_publish(client: Client, userdata, mid):
    print(client._client_id)


def on_disconnect(client, userdata, rc):
    print("return result is " + str(rc))


class MQTTBridge(Client):
    def __init__(self, id: str, filename: str):
        super().__init__(client_id=id)
        self.on_connect = on_connect
        self.on_message = on_message
        self.on_publish = on_publish
        self.on_disconnect = on_disconnect
        self.config_filename = filename


    def start(self):
        self.connect(BROKER_HOST, BROKER_PORT, 60)
        self.loop_start()
        f = open(self.config_filename)
        for topic in f:
            try:
                self.subscribe(topic.strip())
            except ValueError:
                print(topic)

    def finish(self):
        self.loop_stop()
        self.disconnect()

    def get_data(self):
        pass

    def send_data(self):
        pass




