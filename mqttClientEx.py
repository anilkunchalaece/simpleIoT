"""
Author : Kunchala Anil
Email : anillunchalaece@gmail.com

Script is used as a client for adafruit mqtt - it receives commands from
mqtt server and send the same to the Arduino

"""

def connected(mqtt) :
    print("client connected")

def disconnected(mqtt) :
    print("client disconnected")

def message(mqtt,feedId,payload):
    print("received a msg") 


from Adafruit_IO import *
mqtt = MQTTClient('anilkunchalaece','e996656b9fe54f9fa298816e1fb9398f')

#callback functions
mqtt.on_connect = connected
mqtt.on_disconnect = disconnected
mqtt.on_message = message

mqtt.connect()
mqtt.loop_blocking()