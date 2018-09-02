# https://github.com/szazo/DHT11_Python/blob/master/dht11_example.py

import RPi.GPIO as GPIO
import dht11
import time
import datetime
from storeHT import dbtemps

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# print('init db')
writeHT = dbtemps()

# read data using pin 4
getHT = dht11.DHT11(pin=4)
while True:
    result = getHT.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
#        print('trying to write')
        writeHT.write_temp(result.humidity, result.temperature)

    time.sleep(1)
    exit()
