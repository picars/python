#!/usr/bin/env python

""" Must be run as root - sudo python PinTest_11.py """

import time, RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)

#Remember to setup the GPIO pin as input or output 
GPIO.setup(11, GPIO.OUT)

#while True:
print "Just about to set Pin 11 output to 0 to clear"
outputOff = GPIO.output(11, 0)
time.sleep(1)
print "About to set Pin 11 output to 1 to set"
outputOn = GPIO.output(11, 1)
print "Waiting with pin 11 set to 1"
time.sleep(10)

