import Jetson.GPIO as GPIO

M0_PIN = 11
M1_PIN = 12
#AUX_PIN = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(M0_PIN, GPIO.OUT)
GPIO.setup(M1_PIN, GPIO.OUT)
#GPIO.setup(AUX_PIN, GPIO.IN)


# Normal : Mode0
GPIO.output(M0_PIN, GPIO.LOW)
GPIO.output(M1_PIN, GPIO.LOW)

# Wake-up : Mode1 - Not Used
#GPIO.output(M0_PIN, GPIO.HIGH)
#GPIO.output(M1_PIN, GPIO.LOW)

# Power Saving : Mode2 - Not Used
#GPIO.output(M0_PIN, GPIO.LOW)
#GPIO.output(M1_PIN, GPIO.HIGH)

# Sleep : Mode3 for Parameter setting
#GPIO.output(M0_PIN, GPIO.HIGH)
#GPIO.output(M1_PIN, GPIO.HIGH)

