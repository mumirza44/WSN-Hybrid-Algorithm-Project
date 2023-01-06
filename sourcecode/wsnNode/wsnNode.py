#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 23-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""WSN Node file calls the methods from the wsnHybrid Library"""
# ---

import random
import json
from paho.mqtt import client as mqtt_client
from wsnHybrid import WsnHybrid
import requests

broker = '0.0.0.0'
port = 1883
topic = "mqtt/wsn"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


# wsnHybrid Library variables
wsn_xmode = "event-driven"
threshold_xtemp = 50
threshold_start = 5
threshold_stop = 4
mode_counter = 0
timedriven_interval = 10
#node = 

# Create wsn library object
wsn_lib = WsnHybrid(wsn_xmode,threshold_xtemp,threshold_start,threshold_stop,timedriven_interval)
wsn_mode = wsn_lib.orchestrator(30) # Call the orchestrator function in the wsn lib

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    """Subscribe function for MQTT broker"""
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #print(msg.payload.decode())
        x = msg.payload.decode()
        data = json.loads(x)
        print("Temp Received:",data)
        
        wsn_mode = wsn_lib.orchestrator(data)
        print("in wsn node file mode is:",wsn_mode)
        
    client.subscribe(topic)
    client.on_message = on_message
    
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
