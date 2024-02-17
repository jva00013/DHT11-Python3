#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
import requests
DHTPin = 11     #Pin donde se encuentra el DHT11

def loop():
    dht = DHT.DHT(DHTPin)   #Creamos el objeto DHT11
    while(True):
        chk = dht.readDHT11()     #Leemos el DHT11 
        if (chk == dht.DHTLIB_OK):      #Si el dato leído es correcto

            #Mostramos temperatura por la consola
            print("Humedad : %.2f, \t Temperatura : %.2f" % (dht.humidity,dht.temperature))

            #Y construimos la petición HTTP
            headers = {
                'Content-Type': 'application/json',
            }
            data = '{"temperatura": "%.2f", "humedad":"%.2f"}' % (dht.temperature,dht.humidity)

            #Enviamos la petición
            response = requests.post('http://localhost/add', headers=headers, data=data.encode())

            #Mostramos el código de estado de la respuesta: 200 OK
            print(f"Server response: {response.status_code}\n")
        #En cualquier caso, esperamos 2 segundos y volvemos al inicio
        time.sleep(2)       
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  

