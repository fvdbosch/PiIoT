#!/usr/bin/env python

import time
import os
from PIL import Image
from PIL import ImageDraw
from Adafruit_LED_Backpack import Matrix8x8
from sys import argv

# read which symbol is requested
symbol = argv[1]

# define and initialise the display
display = Matrix8x8.Matrix8x8(address=0x71, busnum=1)
display.begin()

# define an image to draw symbols on
image = Image.new('1', (8, 8))
draw = ImageDraw.Draw(image)

if symbol == "sun":
    draw.line((0,0,7,7), fill=255)
    draw.line((7,0,0,7), fill=255)
    draw.rectangle((2,2,5,5), outline=255)
    draw.line((2,2,2,2), fill=0)
    draw.line((2,5,2,5), fill=0)
    draw.line((5,2,5,2), fill=0)
    draw.line((5,5,5,5), fill=0)
    draw.line((0,3,0,3), fill=255)
    draw.line((4,0,4,0), fill=255)
    draw.line((3,7,3,7), fill=255)
    draw.line((7,4,7,4), fill=255)

elif symbol == "cloud":
    draw.line((0,3,0,5), fill=255)
    draw.line((1,1,1,6), fill=255)
    draw.line((2,0,2,6), fill=255)
    draw.line((3,1,3,5), fill=255)

elif symbol == "rain":
    draw.line((0,3,0,5), fill=255)
    draw.line((1,1,1,6), fill=255)
    draw.line((2,0,2,6), fill=255)
    draw.line((3,1,3,5), fill=255)
    draw.line((5,1,7,3), fill=255)
    draw.line((5,3,7,5), fill=255)
    draw.line((5,5,7,7), fill=255)

elif symbol == "radio":
    draw.line((7,0,7,7), fill=255)
    draw.line((3,0,3,7), fill=255)
    draw.line((3,0,7,0), fill=255)
    draw.line((3,7,7,7), fill=255)
    draw.line((3,6,0,3), fill=255)
    draw.line((3,0,3,0), fill=0)
    draw.line((3,7,3,7), fill=0)
    draw.line((7,0,7,0), fill=0)
    draw.line((7,7,7,7), fill=0)

elif symbol == "whoami":
    draw.rectangle((3,0,4,1), outline=255)
    draw.rectangle((3,3,4,4), outline=255)
    draw.rectangle((3,6,4,7), outline=255)

# display the symbol
display.set_image(image.rotate(90))
display.write_display()

time.sleep(10)

# clear the symbol after 10 seconds
display.clear()
display.write_display()
