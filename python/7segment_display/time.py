#!/usr/bin/env python 

import time
from datetime import datetime
from Adafruit_LED_Backpack import SevenSegment

display = SevenSegment.SevenSegment(address=0x70, busnum=1)

colon = False

display.begin()

while True:
  now = datetime.now()

  hours = now.hour
  minutes = now.minute
  seconds = now.second

  string = str(hours) + str(minutes).zfill(2)

  colon = not colon

  display.clear()
  display.print_float(float(string), decimal_digits=0, justify_right=True)
  display.set_colon(colon)
  display.write_display()
  time.sleep(0.5)


