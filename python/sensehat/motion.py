#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

try:
    while True:
        pitch, roll, yaw = sh.get_orientation().values()

        pitch = round( pitch, 1 )
        roll = round( roll, 1 )
        yaw = round( yaw, 1 )

        print( "Pitch = %s°    Roll = %s°    Yaw = %s°" %(pitch, roll, yaw) )

except KeyboardInterrupt:
    print( "Exiting..." );
