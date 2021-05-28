#!/usr/bin/python3
import time
import serial

# Jetson nano 송신부
jet_tx = serial.Serial(
    port='/dev/ttyTHS1',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

num = 0
sleep_rate = 0.5

while True:
    try:
        msg = 'message'.ljust(20, "-") + '[{}]\n'.format(num)
        msg_len = len(msg)
        jet_tx.write(msg.encode())
        print('send_msg[{}], rate: {}byte per {}sec'.format(num, msg_len, sleep_rate))
        num += 1
        time.sleep(sleep_rate)
    except Exception as e:
        print(e)

