#read data from a BME280 Sensor and write it into a LOG<date>.txt file
#
#author Benjamin Koderisch and Christopher Kossatz
#version 1.3 21.04.2016

idpi = '0001'

from time import *
import time
from Adafruit_BME280 import *
import os
from client import sendData
from client import installData
#from client import recv_timeout
import socket
import sys
import struct

#sensor = BME280(mode=BME280_OSAMPLE_8)

def writeDATA(s):
    try:
        #temp = sensor.read_temperature()
        #pascals = sensor.read_pressure()
        #press = pascals / 100
        #hum = sensor.read_humidity()
    except:
        print 'Sensor Error. Please try again.'
    hum = 50
    press = 1000
    temp = 85.3

    t = time.strftime("%Y%m%d%H%M%S", time.localtime())
    sendData(s,t, humidity = hum , pressure = press, temperature=temp)

#input ip
host = "192.168.2.111"
port = 8888

#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

print 'Socket Created'

try:
    remote_ip = socket.gethostbyname( host )
    s.connect((host, port))

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

try :
    #Set the whole string
    installData(s,idpi,["humidity","temperature","pressure"])

    for i in range(5):
    	writeDATA(s)
    	#900 = 15 min
    	time.sleep(2)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

s.close()
