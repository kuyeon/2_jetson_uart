import serial
import time

jetson = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=115200,
    #timeout=1,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

time.sleep(1)

# print(serial_port.portstr)

try:
    while True:
        command_from_jetson = jetson.readline(jetson.inWaiting()).decode()
        print(command_from_jetson)
        jetson.write(('Hello Jetson! this is what I got from you: ' + command_from_jetson).encode())
        time.sleep(1)

except Exception as e:
    print(e)

finally:
    pass