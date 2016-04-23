# WeatherProjekt

Reading Sensor data with a Raspberry Pi Zero and transmitting this data on a server to further analysis.
The Transmission is done via a TCP Socket between the Raspberry Pi Zero and another Linux Machine (Most likely a Raspberry Pi 3) in the same LAN.

##Team

- Analysis/Network: Christopher Kossatz
- Hardware: Nikolaus Herzog
- Software: Benjamin Koderisch

#Setup:

##Client
Connect the Sensor to
SDA -> Pin 3
SCLK -> Pin 5



Make sure that you enable I2C and SPI.
```
sudo raspi-config
-> Advanced Options
  ->I2C
  ->SPI
```
then you can proceed with the install Process:

```
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/Maxklos/WeatherProjekt.git
cd WeatherProjekt/Client
sudo python setup.py install
sudo python ReadData.py
```
##Server

```
sudo apt-get update
git clone https://github.com/Maxklos/WeatherProjekt.git
cd WeatherProjekt/Server
sudo python server.py

```



- We are working on optimising this setup
- We are using the Adafruit Python GPIO Library
