#!/usr/bin/env python

""" Must be run as root - sudo python PinTest_11.py """

import time, RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)

#Remember to setup the GPIO pin as input or output 
GPIO.setup(11, GPIO.OUT)

while True:
	print "Just about to set output to 0"
	outputOff = GPIO.output(11, 0)
	print "Just set output to 0 about to sleep for 1 second"
	time.sleep(1)
	print "Just slept after setting output to 1"
	outputOn = GPIO.output(11, 1)
	print "Just set output to 1 just about to sleep for another 1 second"
	time.sleep(1)

