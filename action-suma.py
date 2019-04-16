#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    if intent_message.intent.intent_name == 'josenka:Suma':
        sentence = 'Quieres sumar '
    elif intent_message.intent.intent_name == 'Suma':
        sentence = 'El resultado es '
    else:
        return
    
    primer_numero = intent_message.slots.firstTerm.first()
    segundo_numero = intent_message.slots.secondTerm.first()
    
    if primer_numero is not None:
        sentence += primer_numero.value
    if segundo_numero is not None:
        sentence +=  'y ' + segundo_numero.value
    
    
    
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
