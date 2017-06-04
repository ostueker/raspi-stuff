#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# map colors to GPIO pins
red   = 17 
green = 18
yellow= 19

# delay in seconds:
delay = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red,    GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green,  GPIO.OUT)

try:
    for i in range(60):
        GPIO.output(red,    False)
        GPIO.output(yellow, False)
        GPIO.output(green,  False)
        if   i%3 == 0:
            GPIO.output(red,    True)
        elif i%3 == 1:
            GPIO.output(yellow, True)
        else:
            GPIO.output(green,  True)
        time.sleep(delay)
finally:
    GPIO.output(red, False)
    GPIO.output(yellow, False)
    GPIO.output(green, False)
