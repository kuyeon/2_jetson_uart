#!/usr/bin/python3
import time
import serial

# Jetson nano 수신부
j_rx = serial.Serial(
    port='/dev/ttyTHS1',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

while True:
    try:
        if j_rx.readable():
            msg = j_rx.readline().decode()
            msg = msg[:len(msg)-1]
            print(msg)

    except Exception as e:
        print(e)
