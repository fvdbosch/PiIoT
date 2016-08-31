#!/usr/bin/env python 

import os
from gpiozero import Button
from time import sleep

pushbutton = Button(26)

while(1):

  if(pushbutton.is_pressed):
    os.system("sudo killall mplayer")

  sleep(0.05)
