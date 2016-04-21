# WeatherProjekt

Reading Sensor data with a Raspberry Pi Zero and transmitting this data on a server to further analysis.
The Transmission is done via a TCP Socket between the Raspberry Pi Zero and another Linux Machine (Most likely a Raspberry Pi 3) in the same LAN.

##Team

- Analysis/Network: Christopher Kossatz
- Hardware: Nikolaus Herzog
- Software: Benjamin Koderisch

#Setup:

##Client

```
sudo apt-get update
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
