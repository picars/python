#!/usr/bin/env python

""" Must be run as root - sudo python PicarsFunctions.py """

import time, datetime, RPi.GPIO as GPIO 

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


def print_time(): #prints out the time now in a format we like
    #print "Time before statement is run"
    print datetime.datetime.now()

def forwards_on(): #turns the forwards pin on
    print "About to turn forwards pin on"
    print_time()
    #turn back off as well
    backwards_off()
    GPIO.output(FORWARD,1)

def forwards_off(): #turns the forwards pin off
    print "About to turn forwards pin off"
    print_time()
    GPIO.output(FORWARD,0)

def backwards_on(): #turns backwards pin on
    print "About to turn the backwards pin on"
    print_time()
    #turn forwards off as well
    forwards_off()
    GPIO.output(BACK,1)

def backwards_off(): #turns backwards pin off
    print "About to turn the backwards pin off"
    print_time()
    GPIO.output(BACK,0)

def left_on(): #turns the left pin on
    print "About to turn the left pin on"
    print_time()
    #turn right off as well
    right_off()
    GPIO.output(LEFT,1)

def left_off(): #turns the left pin off
    print "About to turn the left pin off"
    print_time()   
    GPIO.output(LEFT,0)

def right_on(): #turns the right pin on
    print "About to turn the right pin on"
    print_time()
    #turn left off as well
    left_off()
    GPIO.output(RIGHT,1)

def right_off(): #turns the right pin off
    print "About tot turn the right pin off"
    print_time()
    GPIO.output(RIGHT,0)

def choose_dir(dirWanted=LEFT):
    if dirWanted == LEFT:
        right_off()
        left_on()
    else:
        left_off()
        right_on()

def straighten():
    print "About to straighten"
    print_time()
    left_off()
    right_off()

def slalom(startSideDir=RIGHT,startDir=FORWARD,turns=4, interval=0.1): #does a slalom by default starting right and doing it 4 times with an interval of 0.1
    i = 0
    #need to determine which way we should be going with the direction
    if startDir == FORWARD:
	print "Going to move forwards in the slalom"
        print_time()
        forwards_on()
    else:
	print "Going to move backwards in the slalom"
        print_time()
        backwards_on()
    #now do the turns
    while i < turns:
        print "about to slalom to = ", startSideDir
        choose_dir(startSideDir)
        print "Left direction", LEFT
        print "Right direction", RIGHT
        print_time()
        if i == 0:
            #the first turn should only be half the amount
            time.sleep(interval/2)
        else:
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

def cleanup(): #cleans up the GPIO pins
    GPIO.cleanup()

def sleep(sleepTime=1):
    time.sleep(sleepTime)

#try:
def main():
    try:
        forwards_on()
#        sleep(0.6)
#        right_on()
        sleep(0.5)
        #all_off()
        slalom(LEFT,FORWARD,4,0.5)
        sleep(0.5)
        all_off()
        sleep(0.5)
        #time.sleep(0.4)
        #backwards_on()
        #time.sleep(1)
        slalom(LEFT,BACK,4,0.5)
        sleep(0.5)
        #forwards_on()
        #time.sleep(1)
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
        cleanup()
    except KeyboardInterrupt:
        cleanup()

if __name__ == "__main__":
    main()


   