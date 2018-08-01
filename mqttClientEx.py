"""
Author : Kunchala Anil
Email : anillunchalaece@gmail.com

Script is used as a client for adafruit mqtt - it receives commands from
mqtt server and send the same to the Arduino

"""
from Adafruit_IO import *
import serial
import time

ser = serial.Serial('COM11',115200)
mqtt = MQTTClient('anilkunchalaece','e996656b9fe54f9fa298816e1fb9398f')


FeedId_1 = 'ledControl'
FeedId_2 = 'servoControl'

def connected(mqtt) :
    print("client connected")
    mqtt.subscribe(FeedId_1)
    mqtt.subscribe(FeedId_2)

def disconnected(mqtt) :
    print("client disconnected")

def message(mqtt,feedId,payload):
    print("received a msg")
    # print(feedId)
    # print(payload) 
    if (feedId == 'servoControl') :
        strToSend = '!S'+payload+'@'
        ser.write(strToSend.encode('utf-8'))
    elif (feedId == 'ledControl') :
        if payload == 'ON' :
            strToSend = '!L1@'.encode('utf-8')
        else :
            strToSend = '!L0@'.encode('utf-8')
        ser.write(strToSend)


#callback functions
mqtt.on_connect = connected
mqtt.on_disconnect = disconnected
mqtt.on_message = message

mqtt.connect()
mqtt.loop_background()
while True :
    while ser.in_waiting :
        data = ser.readline()
        print (data)
        try :
            mqtt.publish('potOutput',int(data.strip()))
            print ("published")
            time.sleep(2)
        except :
            print("unable to do it")