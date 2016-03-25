from time import *
import time
#from Adafruit_BME280 import *

#sensor = BME280(mode=BME280_OSAMPLE_8)

#temp = sensor.read_temperature()
#pascals = sensor.read_pressure()
#press = pascals / 100
#hum = sensor.read_humidity()
temp = '20'
press = '30'
hum = '40'

def writeDATA():
	f = open('LOG.txt', 'a')
	
	f.write(time.strftime("%Y%m%d%H%M%S", time.localtime()) + '\n' + 
                'TEMP ' + temp + ' | PRESS ' + press + ' | HUM ' + hum + '\n')
	f.close()

	
while True:
	writeDATA()
	time.sleep(2)
