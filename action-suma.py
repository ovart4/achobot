#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import hermes_python 
import requests

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    if intent_message.intent.intent_name == 'josenka:Suma':
        sentence = 'Tu lo que quieres es sumar'
        print(sentence)

    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
h.subscribe_intents(intent_received).start()
