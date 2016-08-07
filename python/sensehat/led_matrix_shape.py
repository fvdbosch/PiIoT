
#!/usr/bin/env python

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

X = [0, 0, 255]
O = [0, 0, 0]

wink = [
O, X, O, O, O, O, O, O,
X, O, X, O, O, X, X, X,
O, X, O, O, O, O, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, O, O, O, O, O,
O, X, O, O, O, O, X, O,
O, O, X, X, X, X, O, O
]

try:
    sh.set_pixels(wink)

except KeyboardInterrupt:
    print( "Exiting..." );

