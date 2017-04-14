import serial
from time import sleep
ser = serial.Serial('/dev/ttyS0', timeout=1)
ser.baudrate = 115200

msg = 'hello world'
ser.write(msg)
print("Message written")
