import Jetson.GPIO as GPIO

M0_PIN = 11
M1_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(M0_PIN, GPIO.OUT)
GPIO.setup(M1_PIN, GPIO.OUT)

# while True:
GPIO.output(M0_PIN, GPIO.HIGH)
GPIO.output(M1_PIN, GPIO.LOW)