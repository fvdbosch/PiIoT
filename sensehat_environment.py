#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

try:
    while True:
        th = sh.get_temperature()
        tp = sh.get_temperature_from_pressure()
        p = sh.get_pressure()
        h = sh.get_humidity()

        th = round( th, 1 )
        tp = round( tp, 1 )
        p = round( p, 1 )
        h = round( h, 1 )

        print( "Temp (H) = %s°C    Temp (P) = %s°C    Prsr = %smb   Hmdt = %s%%" %(th,tp,p,h) )
        sleep( 1 )

except KeyboardInterrupt:
    print( "Exiting..." );
