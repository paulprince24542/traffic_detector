import serial
import time

arduino = serial.Serial('COM7', 9600)
time.sleep(3)

def serialCom(message):
    arduino.write(message.encode())
    time.sleep(5)

serialCom("redlight")

serialCom("signal1")

serialCom("redlight")

serialCom("signal2")

serialCom("initial")




