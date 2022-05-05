import RPi.GPIO as GPIO
import time
c = 0
dac = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    for c
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
    GPIO.cleanup()