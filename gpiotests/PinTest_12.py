#!/usr/bin/env python

""" Must be run as root - sudo python Blink11.py """

import time, RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while True:
	print "Just about to set output to 0"
	LEDon = GPIO.output(12, 0)
	print "Just set output to 0 about to sleep for 1"
	time.sleep(1)
	print "Just slept after setting output to 1"
	LEDoff = GPIO.output(12, 1)
	print "Just set output to 1 just about to sleep for 1"
	time.sleep(1)

