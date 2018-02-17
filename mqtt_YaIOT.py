#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho
import time

#Publish Callback
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

#Connected Callback
def on_connect(client, userdata, mid):
    print("Connected to the Broker")

#Disconnect Callback
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Lost connection / Disconnected from Broker")

client = paho.Client()
client.on_publish = on_publish #Callback for publish event
client.on_connect = on_connect #Callback for connect event
client.on_disconnect = on_disconnect #Callback for disconnect event
external_broker = "broker.hivemq.com" #Using HiveMQ nice free MQTT broker :)
client.connect(external_broker, port=1883)
client.loop_start() #Non-blocking network interface (yaay)
 
while True:
    for x in range (0, 100):
        msg = "/node/t:10/u:70/uv:1/" + str(x) #Just a sample msg to be published on the topic
        (rc, mid) = client.publish("navarro/yaiot", msg) #Publish on navarro/yaiot topic
        time.sleep(0.5)
