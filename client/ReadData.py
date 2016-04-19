#read data from a BME280 Sensor and write it into a LOG<date>.txt file
#
#author Benjamin Koderisch and Christopher Kossatz
#version 1.2 19.04.2016

from time import *
import time
from Adafruit_BME280 import *
import os
from client import sendData
from client import installData
import socket
import sys
import struct
import time

#sensor = BME280(mode=BME280_OSAMPLE_8)

def writeDATA(s):

        #temp = sensor.read_temperature()
        #pascals = sensor.read_pressure()
        #press = pascals / 100
        #hum = sensor.read_humidity()
        hum = 50
        press = 1000
        temp = 85.3

        t = time.strftime("%Y%m%d%H%M%S", time.localtime())
        sendData(s,t, humidity = hum , pressure = press, temperature=temp)

def recv_timeout(the_socket,timeout=2):
    #make socket non blocking
    the_socket.setblocking(0)

    #total data partwise in an array
    total_data=[];
    data='';

    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break

        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break

        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass

    #join all parts to make final string
    return ''.join(total_data)

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
    installData(["humidity","temperature","pressure"],s)
    m = recv_timeout(s)

    if int(m) == 1:
        print("succesdully installed parameters")

    for i in range(5):
    	writeDATA(s)
        m = recv_timeout(s)

        if int(m) == 1:
            print("Send Data")
        elif int(m) == -1:
            print("Invalid Data")
        else:
            print("Could not transmit Data correctly")
            sys.exit()

    	#900 = 15 min
    	time.sleep(2)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

#get reply and print
print recv_timeout(s)

s.close()
