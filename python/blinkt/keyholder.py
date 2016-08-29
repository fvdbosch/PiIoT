#!/usr/bin/env python 

from blinkt import set_pixel, show
from gpiozero import Button
from time import sleep
import paho.mqtt.client as mqtt

key_1 = Button(26)
key_2 = Button(20)
key_3 = Button(16)
key_4 = Button(19)

client = mqtt.Client()

client.connect("192.168.0.152", 1883, 60)

def blinkt_led(pixel, r, g, b):
  set_pixel(pixel, r, g, b)
  show()

while(1):
  client.reconnect()

  if(key_1.is_pressed):
    blinkt_led(1, 0, 0, 0)
    client.publish("keyholder/key1", "Present")
  else:
    blinkt_led(1, 255, 0, 0)
    client.publish("keyholder/key1", "Absent")

  if(key_2.is_pressed):
    blinkt_led(3, 0, 0, 0)
    client.publish("keyholder/key2", "Present")
  else:
    blinkt_led(3, 0, 255, 0)
    client.publish("keyholder/key2", "Absent")

  if(key_3.is_pressed):
    blinkt_led(5, 0, 0, 0)
    client.publish("keyholder/key3", "Present")
  else:
    blinkt_led(5, 0, 0, 255)
    client.publish("keyholder/key3", "Absent")

  if(key_4.is_pressed):
    blinkt_led(7, 0, 0, 0)
    client.publish("keyholder/key4", "Present")
  else:
    blinkt_led(7, 255, 255, 0)
    client.publish("keyholder/key4", "Absent")

  client.disconnect()

  sleep(5)
