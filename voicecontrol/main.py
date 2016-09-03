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
    symbol = ""
    weather = os.popen('/home/pi/piiotvoice/weather.py').read().lower()
    print weather

    if "sunny" in weather:
        symbol = "sun"
    elif "cloudy" in weather:
        symbol = "cloud"
    elif "showers" in weather:
        symbol = "rain"
   
    setSymbol(symbol)
    playResponse(weather)

def getContact(room):
    sensor = ""
    shed_sensor = "EnOcean_sensor_0180FC58"
    lab_sensor = "EnOcean_sensor_0180AAFA"

    if room == "shed":
        sensor = shed_sensor
    elif room == "lab":
        sensor = lab_sensor

    contact = os.popen("curl http://192.168.0.152:8080/rest/items/" + sensor + "/state").read()
    playResponse("the door of the " + room + " is " + contact)

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
    os.system("/home/pi/piiotvoice/symbol.py " + symbol + " &")

def thankYou():
    playResponse("You're welcome")

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

            print "command: " + command

            if "time" in command:
                getTime()
            elif "temperature" in command:
                if "shed" in command:
                    getTemperature("shed")
                if "lab" in command:
                    getTemperature("lab")
            elif "door" in command:
                if "shed" in command:
                    getContact("shed")
                if "lab" in command:
                    getContact("lab")
            elif "radio" in command:
                if "turn on" in command:
                    turnOnRadio()
                if "turn off" in command:
                    turnOffRadio()
            elif "weather" in command:
                getWeather()
            elif "who are you" in command:
                whoAmI()
            elif "thank you" in command:
                thankYou()

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
