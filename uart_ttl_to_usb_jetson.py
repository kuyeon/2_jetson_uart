#!/usr/bin/python3
import time
import serial


laptop = serial.Serial(
    port='/dev/ttyTHS1',
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

try:
    while True:
        laptop.write('Jetson Nano Command'.encode())
        ackmsg_from_laptop = laptop.readline(laptop.inWaiting()).decode()
        print(ackmsg_from_laptop)
        time.sleep(1)

except Exception as e:
    print(e)

finally:
    pass