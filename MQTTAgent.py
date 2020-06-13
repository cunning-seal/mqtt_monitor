from paho.mqtt.client import topic_matches_sub
from zabbix_sender import Metric, send_to_zabbix
from config import *
import logging

class MQTTAgent:
    def __init__(self):
        pass

    def key_mapping(self, config_filename):
        self.config_filename = config_filename
        self.key_mapping = {}
        f = open(config_filename)
        for config_row in f:
            data = config_row.split(' ')
            self.key_mapping.update({data[0].strip(): data[1].strip()})


    def process_data(self, topic, value):
        for subscription, key in self.key_mapping.items():
            if topic_matches_sub(subscription, topic):
                send_to_zabbix([Metric(MQTT_AGENT_HOST_NAME, key, value[1:])],
                               ZABBIX_SERVER_HOST,
                               ZABBIX_SERVER_PORT
                               )
                return True

        logging.error("No such subscription: {}".format(topic))
        return False
