#!/usr/bin/env python

import time
import os
import Adafruit_Trellis

trellis = Adafruit_Trellis.Adafruit_TrellisSet(Adafruit_Trellis.Adafruit_Trellis())
trellis.begin((0x72, 1))

for i in range(16):
        trellis.clrLED(i)
        trellis.writeDisplay()
        time.sleep(0.05)

os.system("sudo killall chromium-browser ; chromium-browser --display=:0 --noerrdialogs --kiosk --disable-pinch --overscroll-history-navigation=0 http://localhost:8080/basicui/app?sitemap=general http://localhost:8080/basicui/app?sitemap=lab http://localhost:8080/basicui/app?sitemap=shed http://www.standaard.be &")

j = 0
trellis.setLED(0)

while True:
  time.sleep(0.03)

  if trellis.readSwitches():
    for i in range(0, 4):
      if trellis.justPressed(i):
        trellis.clrLED(j)
        trellis.setLED(i)
        j = i
        os.system("xte 'keydown Control_L' 'key " + str(i+1) + "' -x:0")
        trellis.writeDisplay()
