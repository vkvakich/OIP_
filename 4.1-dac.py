import RPi.GPIO as GPIO
c = 0
dac = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimalToBinary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        c = int(input())
        GPIO.output(dac, decimalToBinary(c))
        print("Voltage: ", (3.3 / 256) * c)
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
    GPIO.cleanup()