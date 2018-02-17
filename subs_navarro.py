import paho.mqtt.client as paho
import time

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
 
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
external_broker = "broker.hivemq.com"
client.connect(external_broker, port=1883)
client.subscribe("navarro/yaiot", qos=1)
 
client.loop_forever() #Testing blocking client type
