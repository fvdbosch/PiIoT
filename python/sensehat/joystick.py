#!/usr/bin/env python

import pygame

pygame.init()
pygame.display.set_mode((640, 480))

try:
    while True:
        for event in pygame.event.get():
            print(event.key)

except KeyboardInterrupt:
    print( "Exiting..." );
