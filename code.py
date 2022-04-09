bytes = bytearray(b'\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\x00\x004\x04!\x03\x00\x00\x00\x08\x02\x01\x03\xbe\xaa\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\x00\x008\x04!\x03\x00\x00\x00\x08\x02\x01\x03Mc\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\x00\x000\x04!\x03\x00\x00\x00\x08\x02\x01\x03\xef\xed\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\x00\x00h\x04!\x03\x00\x00\x00\x08\x02\x01\x03\\\x8b\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\x00\x00E\x04!\x03\x00\x00\x00\x08\x02\x01\x03\xddq\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\x00\x00\x00\x04!\x03\x00\x00\x00\x08\x02\x01\x03\x10\xaa\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\xff\xff\x9a\x04!\x03\x00\x00\x00\x08\x02\x01\x03\xe6\x0c\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\xff\xff\x88\x04!\x03\x00\x00\x00\x08\x02\x01\x03\x13\x82\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\xff\xff\x97\x04!\x03\x00\x00\x00\x08\x02\x01\x03\xcd\x8c\xc2\xc2\xc2\x11\x15\x04\x01\x02\x00\x00\x04\x00\x03\xff\xff\xf0\x04!\x03\x00\x00\x00\x08\x02\x01\x03\n')
# if b'\xc2' in bytes:
#     print(bytes.index(b'\xc2'))
'''
client: A Macawi module or device
host: The other side of the communication channel. This can be a PC or an apparatus which controls the Macawi module or device.
A packet of data in a stream will be delimited by corresponding END1, END2, END3 or END4 byte of the stream.
\xc0    192     ESC
\xc1    193     END1    EVENT
\xc2    194     END2    REAL-TIME
\xc3    195     END3    BREADTH-DATA
\xc4    196     END4    DATA
If the END-Byte occurs in the data packet to be transmitted, a two byte sequence ESC and the corresponding ESC_END-Byte, is transmitted instead. If the ESC byte occurs in the data to be transmitted, the two byte sequence ESC, ESC_ESC is transmitted instead.
\xd0    208     ESC_ESC
\xd1    209     ESC_END1
\xd2    210     ESC_END2
\xd3    211     ESC_END3
\xd4    212     ESC_END4

'''
# import sys
# print(int.from_bytes(b'\xd2', byteorder=sys.byteorder) )
# #bin(int.from_bytes(b'\xc0', byteorder=sys.byteorder))  # => '0b10001'



# event_stream=[]
# real_time_stream =[]
# breadth_data_stream=[]
# data=[]

# def save_stream(bytes):
#     '''Save the stream to log file for future calculation'''
#     file = open('respiratory.log','wb')
#     file.write(bytes)

# def device(port):
#     obj = serial.Serial(port)
#     obj.baudrate = 1000000 
#     obj.bytesize = 8
#     obj.parity = 'N'
#     obj.stopbits =1
#     return obj

# def offline_data():
#     file = open("respiratory.log","rb")
#     return file
# def start_realtime_stream(obj):
#     obj.write(b'\x04')
#     ack_nack = obj.read()
#     if ack_nack ==b'\x21':
#         print('ACK recieved')
#     elif ack_nack == b'\x23':
#         print('NACK Recieved')
file = open("respiratory.log","rb")

byteline = file.readline()
print(len(byteline))
