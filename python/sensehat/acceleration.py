#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

try:
    while True:
        x, y, z = sh.get_accelerometer_raw().values()

        x = round( x, 0 )
        y = round( y, 0 )
        z = round( z, 0 )

        print( "X = %s    Y = %s    Z = %s" %(x, y, z) )

except KeyboardInterrupt:
    print( "Exiting..." );
