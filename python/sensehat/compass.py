#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

try:
    while True:
        north = sh.get_compass()
        north = round( north, 1 )

        print( "North = %s°" %(north) )

except KeyboardInterrupt:
    print( "Exiting..." );
