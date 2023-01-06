#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 21-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""Temperature Simulator - Sends Temperature Telemetry over MQTT """
# ---


import time
import random
from paho.mqtt import client as mqtt_client

broker = '0.0.0.0'
port = 1883
topic = "mqtt/wsn"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
     msg_count = 0
     while True:
         time.sleep(1)
       

         #msg = random.randint(40, 49)
         msg = random.randint(51, 60)
         
         print(msg)
         result = client.publish(topic, msg)
         # result: [0, 1]
         status = result[0]
         if status == 0:
             print(f"Send `{msg}` to topic `{topic}`")
         else:
             print(f"Failed to send message to topic {topic}")
         msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
