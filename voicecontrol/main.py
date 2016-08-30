#!/usr/bin/env python


# Original code by Neil Davenport for Make:
# http://makezine.com/projects/use-raspberry-pi-for-voice-control/
#
# Modified by Frederick Vandenbosch for element14's PiIoT Design Challenge


import time
from datetime import datetime
import os
import subprocess
import sys, traceback
from pocket_sphinx_listener import PocketSphinxListener


def getTime():
    now = datetime.now()
    playResponse("it is " + now.strftime("%I:%M %p"))

def getTemperature(room):
    sensor = ""
    shed_sensor = "EnOcean_sensor_0181B05F"
    lab_sensor = "EnOcean_sensor_01809DC"

    if room == "shed":
        sensor = shed_sensor
    elif room == "lab":
        sensor = lab_sensor

    temperature = os.popen("curl http://192.168.0.152:8080/rest/items/" + sensor + "/state").read()
    playResponse("it is " + str(temperature)[:4] + " degrees in the " + room)

def getWeather():
    weather = os.popen('/home/pi/piiotvoice/weather.py').read()
    #setSymbol(symbol)
    playResponse(weather)

def getContact(door):
    sensor = ""
    shed_sensor = "EnOcean_sensor_0180FC58"
    lab_sensor = "EnOcean_sensor_0180AAFA"

    if room == "shed":
        sensor = shed_sensor
    elif room == "lab":
        sensor = lab_sensor

    contact = os.popen("curl http://192.168.0.152:8080/rest/items/" + sensor + "/state").read()
    playResponse("the door of the " + door + " is " + contact)

def turnOnLight(room):
    return ""

def turnOffLight(room):
    return ""

def turnOnRadio():
    os.system("nohup sleep 2 && sudo mplayer -ao pulse http://icecast-qmusic.cdp.triple-it.nl/Qmusic_be_live_96.mp3 -af volume=-10 &")
    setSymbol("radio")
    playResponse("certainly")

def turnOffRadio():
    os.system("sudo killall mplayer")

def setSymbol(symbol):
    os.popen("/home/pi/piiotvoice/symbol.py " + symbol + " &")

def whoAmI():
    setSymbol("whoami")
    playResponse("I'm a speaking alarm clock, created by Frederick Vandenbosch, for element 14's Pi IOT design challenge")

def playResponse(response):
    os.system("/home/pi/piiotvoice/response.py \"" + response + "\"")

def runMain():
    pocketSphinxListener = PocketSphinxListener()

    while True:
        try:
            command = pocketSphinxListener.getCommand().lower()
            command = command.replace('the', '')
            command = command.replace('what', '')
            command = command.replace('of', '')
            command = command.replace('is', '')
            command = command.replace('will', '')
            command = command.replace('be', '')
            command = command.replace('like', '')
            command = command.replace('it', '')
            command = command.replace('open', '')
            command = command.replace('closed', '')
            command = command.replace(' ', '')

            print "command: " + command

            if command.startswith('time'):
                getTime()

            elif command.startswith('temperature'):
                command = command.replace('temperature', '')
                getTemperature(command)

            elif command.startswith('door'):
                command = command.replace('door', '')
                getContact(command)            

            elif command.startswith('turnon'):
                command = command.replace('turnon', '')

                if command.startswith('light'):
                    command = command.replace('light', '')
                    turnOnLight(command)

                elif command.startswith('radio'):
                    turnOnRadio()

            elif command.startswith('turnoff'):
                command = command.replace('turnoff', '')

                if command.startswith('light'):
                    command = command.replace('light', '')
                    turnOffLight(command)

                elif command.startswith('radio'):
                    turnOffRadio()

            elif command.startswith('wear'):
                getWeather()

            elif command.startswith('thankyou'):
                response = "you're welcome"

            elif command.startswith('whoareyou') or command.startswith('areyou'):
                whoAmI()                


        except (KeyboardInterrupt, SystemExit):
            print 'People sometimes make mistakes, Goodbye.'
            sys.exit()

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=2,
                                      file=sys.stdout)
            sys.exit()


if __name__ == '__main__':
    runMain()
