#!/usr/bin/env python

import os
from sys import argv

# read which string should be converted to voice
response = argv[1]

# check if there is internet connectivity
def check_internet():
        host = "google.com"
        connectivity = os.system("ping -W 1 -c 1 " + host)

        return connectivity

# if no internet, use local TTS
def offline_response():
        os.system("flite -voice slt -t \"" + response + "\"")

# if internet, use online TTS
def online_response():
        url = "\"http://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=" + response + "\""
        agent = "\"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0\""
        recording = "/tmp/recording.mp3"
	
	# download audio file and play it        
        os.system("wget -U " + agent + " -O " + recording + " " + url + "  && sudo mplayer -ao pulse " + recording + "")

def main():
        if check_internet() == 0:
                online_response()
        else:
                offline_response()

main()
