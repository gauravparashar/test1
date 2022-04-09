from re import S
from time import time
from turtle import clear, fd
import serial
import time

EVENT_END = '0xc1'
REALTIME_END = '0xc2'
BREADTHDATA_END = '0xc3'
DATA_END = '0xc4'
ESC = '0xc0'
###############################################################################################################################
class Serial:
    '''
    Serial Communication with USART 
    '''
    def __init__(self,port):
        self.serialFD = serial.Serial(port=port,baudrate=100000, bytesize=8,parity='N',stopbits=1, xonxoff=False, rtscts=False)
        if self.serialFD < 0:  
            print("Couldn't open serial port")  
            return -1
    def stream_type(self,stream):
        for i in range(0,len(stream)):
            if stream[i] == b'\xc0':
                print("ESC")
            elif stream[i] == b'\xc1':
                print('EVENT END')
            elif stream[i] == b'\xc2':
                print('REAL-TIME END')
            elif stream[i] == b'\xc3':
                print('BREADTH-DATA END') 
            elif stream[i] == b'\xc4':
                print('DATA END')
            




###############################################################################################################################
class File:
    ''' 
    To read and write Data stored in files
    ''' 
    Action_Frame = []
    try:
        def __init__(self,file_name):
            self.file = open(file_name,'rb')
        def write(self,data):
            self.file = open('respiratory.log','wb')
            self.file.write(data)
        def read(self):
            return(self.file.readline())
        def stream_type(self,stream):
            i = 0
            temp = []
            while i < len(stream)-1:
                if hex(stream[i]) == ESC:
                    print("(ESC)",end='')
                elif hex(stream[i]) == EVENT_END:
                    print('(EVENT-END)',end='')
                    EVENT_frame = 1

                elif hex(stream[i]) == REALTIME_END and hex(stream[i+1]) == REALTIME_END:
                    print('(REAL-TIME-START)',end='')
                    REALTIME_frame = 1

                elif hex(stream[i]) == BREADTHDATA_END:
                    print('(BREADTH-DATA-END)',end='') 
                    BREADTH_DATA_frame = 1
                    
                elif hex(stream[i]) == DATA_END:
                    print('(DATA-END)',end='')
                    DATA_STREAM_frame = 1
                  
                if REALTIME_frame == 1:
                    while hex(stream[i]) == REALTIME_END:
                        i = i + 1
                       #print(hex(stream[i]),end=' ')
                    
                    while hex(stream[i]) != REALTIME_END:
                        temp.append(hex(stream[i]))
                        #print(hex(stream[i]),end=' ')
                        i = i + 1
                        '''For breaking the code at index 270 because at 278 there is index error'''
                        if i >= 270:
                            print(i)
                    
                    self.Action_Frame.append(temp)
                    if hex(stream[i]) == REALTIME_END:
                        REALTIME_frame = 0
                        i = i + 1
            for k in range(0,len(self.Action_Frame)-1):
                print('Value of K=',k,"length of frame=",len(self.Action_Frame[k]))
##
    except IOError:
        print("Error: can\'t find file or read data")
    except FileNotFoundError:
        print("Error: File does not exist")
    
#############################################################################################################################

########################################################
if __name__ == "__main__":
    filediscp = File('respiratory.log')
    bytes = filediscp.read()
    #print(bytes)
    filediscp.stream_type(bytes)