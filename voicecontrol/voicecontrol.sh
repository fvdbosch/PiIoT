#!/bin/sh

# loop to check if voice application is still running
while true; do
	ps auxw | grep main.py | grep -v grep > /dev/null

	# if application not running, start it
	if [ $? != 0 ]
	then
		cd /home/pi/piiotvoice/ 
		sudo ./main.py > /dev/null
	fi

	sleep 1
done
