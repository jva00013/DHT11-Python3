#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description :	read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2020/10/16
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
import requests
DHTPin = 11     #define the pin of DHT11

def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    while(True):
        chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        if (chk == dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))

            headers = {
                'Content-Type': 'application/json',
            }
            data = f'{"temperatura": "{dht.humidity}", "humedad":"{dht.temperature}"}'.encode()
            response = requests.post('http://localhost/add', headers=headers, data=data)
            print(f"Server response: {response.status_code}")
        time.sleep(2)       
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  

