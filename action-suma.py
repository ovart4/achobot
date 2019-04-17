#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    if intent_message.intent.intent_name == 'josenka:Suma':
        sentence = 'La suma de'
    else:
        return
    
    primer = intent_message.slots.firstTerm.first().value
    segundo = intent_message.slots.secondTerm.first().value
    suma = primer + segundo
    
    sentence += " : {}".format(str(primer))
    #sentence += " y ".format(str(segundo))
    #sentence += " es ".format(str(suma))
    
    
    
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
