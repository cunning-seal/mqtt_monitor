def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_disconnect(client, userdata, rc):
    print("return result is " + str(rc))
from paho.mqtt.client import Client
def on_publish(client: Client, userdata, mid):
    print(client._client_id)

from paho.mqtt.client import Client
from config import *
import logging
from MQTTAgent import MQTTAgent

logging.basicConfig(level=logging.WARNING, filename=ERROR_LOG_FILE_NAME)

agent_obj = MQTTAgent()

def on_message(client, userdata, msg):
    agent_obj.process_data(msg.topic, str(msg.payload))
    print(msg.payload)

class MQTTBridge(Client):
    def __init__(self, config_filename, id=MQTT_BRIDGE_ID):
        super().__init__(client_id=id)
        self.on_connect = on_connect
        self.on_message = on_message
        self.on_publish = on_publish
        self.on_disconnect = on_disconnect
        self.config_filename = config_filename
        agent_obj.key_mapping(config_filename)

    def start(self, host=MQTT_BROKER_HOST, port=MQTT_BROKER_PORT):
        self.connect(host, port, 60)
        self.loop_start()
        f = open(self.config_filename)
        for config_row in f:
            topic = config_row.split(' ')[0]
            try:
                self.subscribe(topic.strip())
            except ValueError:
                logging.error("Can't subscribe to topic: {}, invalid topic".format(topic.strip()))

    def finish(self):
        self.loop_stop()
        self.disconnect()
