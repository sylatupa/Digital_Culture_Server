import time
import os
import subprocess
import paho.mqtt.client as mqtt
import json


broker_address="192.168.1.115"
mqtt_topic="sensor"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-7")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)   
    #playSingleShot()
    obj = json.loads(str(message.payload.decode("utf-8")))    
    val = obj['v']
    print("received ", val)
    send2Pd(val)


def send2Pd(message=''):
    os.system("echo '" + message + "' | /Applications/Pd-0.48-1.app/Contents/Resources/bin/pdsend 3000 localhost udp")


print("creating new mqtt client instance")
client = mqtt.Client("Luke")

print("connecting to broker")
client.connect(broker_address, 1883)

print("Subscribing to topic",mqtt_topic)
client.subscribe(mqtt_topic)

print("Publishing message to topic",mqtt_topic)
#client.publish(mqtt_topic,"Hallo!!!")

client.on_message=on_message
client.loop_start()

while True:
        print(".")
        #client.publish(mqtt_topic,"Hallo!!!")
        time.sleep(3)
