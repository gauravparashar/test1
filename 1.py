from time import time
import serial
import time
def device(port):
    obj = serial.Serial(port)
    obj.baudrate = 1000000 
    obj.bytesize = 8
    obj.parity = 'N'
    obj.stopbits =1
    return obj

def offline_data():
    file = open("respiratory.log","r")
    return file
#obj = device("/dev/ttyUSB0")
obj = offline_data()
#while True:
recievestr = obj.readline()
print(recievestr)

obj.close()