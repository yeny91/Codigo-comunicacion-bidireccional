#Este codigo sirve para enviar un comando desde python a arduino y recibir un mensaje
#Este codigo se realizo basado en el siguiente tutorial: https://geekytheory.com/arduino-raspberry-pi-raspduino


import serial
import time

arduino=serial.Serial('/dev/ttyUSB0',baudrate=9600, timeout = 3.0)

txt=''

while True:
      comando=input("Introducir un Comando: ")      
      arduino.write(comando.encode())
      time.sleep(0.1)
      while arduino.inWaiting() > 0:
            txt= arduino.readline()
            print (txt)
            txt = ''
