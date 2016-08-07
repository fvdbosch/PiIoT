#!/usr/bin/env python

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

try:
    sh.set_rotation(0)
    sh.show_message("test")
    sleep( 1 )
    sh.set_rotation(90)
    sh.show_message("test", text_colour=[255, 0, 0])
    sleep( 1 )
    sh.set_rotation(180)
    sh.show_message("test", text_colour=[255, 255, 0], back_colour=[0, 0, 255])
    sleep( 1 )
    sh.set_rotation(270)
    sh.show_message("test", scroll_speed=0.5)
    sleep( 1 )

except KeyboardInterrupt:
    print( "Exiting..." );
