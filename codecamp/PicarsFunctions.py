#!/usr/bin/env python

""" Must be run as root - sudo python PinTest_11.py """

import time, RPi.GPIO as GPIO 

FORWARD=12
BACK=11
LEFT=13
RIGHT=15
TURBO=7

GPIO.setmode(GPIO.BOARD)
#Remember to setup the GPIO pin as input or output 
GPIO.setup(FORWARD, GPIO.OUT)
GPIO.setup(BACK, GPIO.OUT)
GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)


def forwards_on(): #turns the forwards pin on
    print "About to turn forwards pin on"
    #turn back off as well
    backwards_off()
    GPIO.output(FORWARD,1)

def forwards_off(): #turns the forwards pin off
    print "About to turn forwards pin off"
    GPIO.output(FORWARD,0)

def backwards_on(): #turns backwards pin on
    print "About to turn the backwards pin on"
    #turn forwards off as well
    forwards_off()
    GPIO.output(BACK,1)

def backwards_off(): #turns backwards pin off
    print "About to turn the backwards pin off"
    GPIO.output(BACK,0)

def left_on(): #turns the left pin on
    print "About to turn the left pin on"
    #turn right off as well
    right_off()
    GPIO.output(LEFT,1)

def left_off(): #turns the left pin off
    print "About to turn the left pin off"
    GPIO.output(LEFT,0)

def right_on(): #turns the right pin on
    print "About to turn the right pin on"
    #turn left off as well
    left_off()
    GPIO.output(RIGHT,1)

def right_off(): #turns the right pin off
    print "About tot turn the right pin off"
    GPIO.output(RIGHT,0)

def choose_dir(dirWanted=LEFT):
    if dirWanted == LEFT:
        right_off()
        left_on()
    else:
        left_off()
        right_on()

def straighten():
    left_off()
    right_off()

def slalom(startSideDir=RIGHT,startDir=FORWARD,turns=4, interval=0.1): #does a slalom by default starting right and doing it 4 times with an interval of 0.1
    i = 0
    #need to determine which way we should be going with the direction
    if startDir == FORWARD:
        forwards_on()
    else:
        backwards_on()
    #now do the turns
    while i < turns:
        print "about to slalom to = ", startSideDir
        choose_dir(startSideDir)
        print "Left direction", LEFT
        print "Right direction", RIGHT
        time.sleep(interval)
        #toggle direction for next time
        if startSideDir == RIGHT:
            startSideDir = LEFT
        else:
            startSideDir = RIGHT
        i = i + 1
    #at the end straighten the wheels
    straighten()    
    

def all_off(): #turns all of the pins off - always call at the end to save battery :)
    GPIO.output(FORWARD,0)
    GPIO.output(BACK,0)
    GPIO.output(LEFT,0)
    GPIO.output(RIGHT,0)

print "About to call some functions"

forwards_on()
time.sleep(0.3)
slalom(RIGHT,FORWARD,5,0.2)
time.sleep(0.4)
backwards_on()
time.sleep(0.7)
#forwards_on()
#time.sleep(0.5)
#right_on()
#time.sleep(0.5)
#right_off()
#time.sleep(0.5)
#left_on()
#time.sleep(0.5)
#left_off()
#time.sleep(0.5)
#forwards_off()
#time.sleep(0.5)
#backwards_on()
#time.sleep(1)
all_off()
#while True:
#    print "Just about to set output to 0"
#    forwards_off()
#    #outputOff = GPIO.output(11, 0)
#    print "Just set output to 0 about to sleep for 1 second"
 #   time.sleep(1)
 #   print "Just slept after setting output to 1"
#    forwards_on()
#    #outputOn = GPIO.output(11, 1)
#    print "Just set output to 1 just about to sleep for another 1 second"
#    time.sleep(1)



    
