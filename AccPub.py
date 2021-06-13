import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime
from time import sleep
import re
from pynput import keyboard
import socket, traceback
import time


def on_press(key):
    global break_program
    print(key)
    if key == keyboard.Key.esc:
        print('end pressed')
        break_program = True
    return False


def map_msg_to_json(lst, addr,pos):
    dic = {}
    dic['Sensor_ID'] = 'Acceleration ' + str(addr)
    dic['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    dic['accX'] = lst[pos].strip()
    dic['accY'] = lst[pos+1].strip()
    dic['accZ'] = lst[pos+2].strip()
    return json.dumps(dic)


def on_connect(client, userdata, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_publish(client, userdata, mid):
    pass


def on_disconnect(client, userdata, rc):
    if rc != 0:
        pass


def publish_to_topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
    print("")


# MQTT Settings
MQTT_Broker = "mqtt.groov.com"
MQTT_Port = 1883
Keep_Alive_Interval = 30

MQTT_Topic_Acc = "Home/BedRoom/Topics/Acceleration"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
break_program = False
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
syntax = {
  1:  ['gps', 'lat', 'lon', 'alt'],     # deg, deg, meters MSL WGS84
  3:  ['accel', 'x', 'y', 'z'],         # m/s/s
  4:  ['gyro', 'x', 'y', 'z'],          # rad/s
  5:  ['mag', 'x', 'y', 'z'],           # microTesla
  6:  ['gpscart', 'x', 'y', 'z'],       # (Cartesian XYZ) meters
  7:  ['gpsv', 'x', 'y', 'z'],          # m/s
  8:  ['gpstime', ''],                  # ms
  81: ['orientation', 'x', 'y', 'z'],   # degrees
  82: ['lin_acc',     'x', 'y', 'z'],
  83: ['gravity',     'x', 'y', 'z'],   # m/s/s
  84: ['rotation',    'x', 'y', 'z'],   # radians
  85: ['pressure',    ''],              # ???
  86: ['battemp', ''],                  # centigrade

# Not exactly sensors, but still useful data channels:
 -10: ['systime', ''],
 -11: ['from', 'IP', 'port'],
}

#dic = {}
with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        try:
            #message, address = s.recvfrom(8192)
            message, (peerIP, peerport) = s.recvfrom(8192)
            lst = re.split("[,\'']", str(message))
            print(message)
            #print(lst[2])
            if int(lst[2])==1 :
            	pos=7
            	Acc_Json_Data = map_msg_to_json(lst, peerIP,pos)
            	publish_to_topic(MQTT_Topic_Acc, Acc_Json_Data)
            	print(message)
            	print(peerIP,'  ',Acc_Json_Data)
            	sleep(1)  # make a pause
            elif int(lst[2])==3:
            	pos=3
            	Acc_Json_Data = map_msg_to_json(lst, peerIP,pos)
            	publish_to_topic(MQTT_Topic_Acc, Acc_Json_Data)
            	print(message)
            	print(peerIP,'  ',Acc_Json_Data)
            	sleep(1)  # make a pause
        except:
        	traceback.print_exc()
    listener.join()
