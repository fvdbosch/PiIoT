#!/usr/bin/env python

import os
from sys import argv

response = argv[1]

def check_internet():
        host = "google.com"
        connectivity = os.system("ping -W 1 -c 1 " + host)

        return connectivity

def offline_response():
        os.system("flite -voice slt -t \"" + response + "\"")

def online_response():
        url = "\"http://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=" + response + "\""
        agent = "\"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0\""
        recording = "/tmp/recording.mp3"
        
        os.system("wget -U " + agent + " -O " + recording + " " + url + "  && sudo mplayer -ao pulse " + recording + "")
        #os.system("wget -U " + agent + " -O " + recording + " " + url + "  && mplayer -ao alsa:device=hw=1.0 " + recording + "")
        #os.system("wget -U " + agent + " -O " + recording + " " + url + "  && omxplayer -o local " + recording + "")

def main():
        if check_internet() == 0:
                online_response()
        else:
                offline_response()

main()
