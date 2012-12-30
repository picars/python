#!/usr/bin/env python

""" Must be run as root - sudo python PiCar_Scratchet.py """
""" Script based on original version from Simon Walters http://cymplecy.wordpress.com """
""" Modified slightly when troubleshooting. Currently only is doing GPIO outputs in order to simplify """

import time, RPi.GPIO as GPIO 
import socket
import sys
import threading
import time
import sys
import struct
from array import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(7,0)
GPIO.output(11,0)
GPIO.output(12,0)
GPIO.output(13,0)
GPIO.output(15,0)

PORT = 42001
DEFAULT_HOST = '127.0.0.1'
#HOST = askstring('Scratch Connector', 'IP:')
BUFFER_SIZE = 240 #used to be 100
SOCKET_TIMEOUT = 1

SCRATCH_SENSOR_NAME_OUTPUT = (
'gpio-output0',
'gpio-output1',
'gpio-output2',
'gpio-output3',
'gpio-output4'
)

#Map gpio to real connector P1 Pins
GPIO_PINS = array('i',[7,11,12,13,15])
GPIO_PIN_OUTPUT = array('i')
GPIO_PIN_INPUT = array('i')
#print "Output Pins are:"
#for i in range(0,len(SCRATCH_SENSOR_NAME_OUTPUT)):
#	print GPIO_PINS[i]
#	GPIO_PIN_OUTPUT.append(GPIO_PINS[i])


def create_socket(host, port):
    while True:
        try:
            #print 'Trying'
            scratch_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scratch_sock.connect((host, port))
            break
        except socket.error:
            print "I am trying to connect to Scratch but cannot - it probably has not been started yet. Double click on the Scratch icon to launch it"
	    print "If you have started Scratch and this message is still continually appearing then shut this by pressing CTR + C and start again"
            #print "I am currently looking for Scratch at host: %s, port: %s" % (host, port)
            time.sleep(3)
            #sys.exit(1)

    return scratch_sock

def cleanup_threads(thread):
	print 'About to stop thread'
	thread.stop()
	GPIO.cleanup()
	print 'Finished cleanup'

class ScratchListener(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.scratch_socket = socket
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def physical_pin_update(self, pin_index, value):
        physical_pin = GPIO_PIN_OUTPUT[pin_index]
        print 'setting GPIO %d (physical pin %d) to %d' % (pin_index,physical_pin,value)
        GPIO.output(physical_pin, value)

    def run(self):
	    while not self.stopped():
		    try:
			    data = self.scratch_socket.recv(BUFFER_SIZE)
			    dataraw = data[4:].lower()
			    print 'Length: %d, Data: %s' % (len(dataraw), dataraw)
			    print 'received something: %s' % dataraw
#			    time.sleep(0.2)
		    except socket.timeout:
			    #print 'Socket timeout'
			    continue
		    except:
			    break
		    if 'sensor-update' in dataraw:
			    print 'Sensor update detected'
			    #check for individual port commands
			    for i in range(len(SCRATCH_SENSOR_NAME_OUTPUT)):
				     if 'gpio-output'+str(i) in dataraw:
					     print 'Found '+ 'gpio-output'+str(i)
					     outputall_pos = dataraw.find('gpio-output'+str(i))
					     sensor_value = dataraw[(outputall_pos+14):].split()
					     #print sensor_value[0]
					     self.physical_pin_update(i,int(sensor_value[0]))



if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST

    # open the socket
    print '*****************************************************************************'
    print '*****************************************************************************'
    print ' '
    print 'Welcome to the Pi-Car Scratchet - helping you connect your Pi-Car to Scratch'
    print 'Visit www.pi-cars.com for more info or email info@pi-cars.com for any questions'
    print ' '
    print '*****************************************************************************'
    print '*****************************************************************************'
    print 'Attempting to connect...' ,
    the_socket = create_socket(host, PORT)
    print 'Connected to Scratch - Scratchet ready to go - check www.pi-cars.com and visit the Under the Bonnet section to see how to connect to a Pi-Car and program Scratch'
    print 'Press CTR + C to close the terminal - you can double click the Scratchet logo again to start it up'    
    the_socket.settimeout(SOCKET_TIMEOUT)
    listener = ScratchListener(the_socket)
    listener.start()
    #print 'Starting cleaner'
    try:
	    while True:
		    time.sleep(0.5)
    except KeyboardInterrupt:
	    cleanup_threads(listener)
	    sys.exit()


