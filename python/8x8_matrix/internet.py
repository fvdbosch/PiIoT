#!/usr/bin/env python 

import time
import os
from PIL import Image
from PIL import ImageDraw
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8(address=0x71, busnum=1)

display.begin()

image = Image.new('1', (8, 8))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,7,7), outline=255, fill=0)
draw.line((1,1,6,6), fill=255)
draw.line((1,6,6,1), fill=255)

while True:
  host = "google.com"
  response = os.system("ping -W 1 -c 1 " + host)

  if response == 0:
    display.clear()
  else:
    display.set_image(image)

  display.write_display()
  time.sleep(0.1)
