import RPi.GPIO as GPIO
from time import sleep

# General setup for GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Pins connected to LEDs
bit0 = 16
bit1 = 15
bit2 = 13
bit3 = 11

# Pin modes

GPIO.setup(bit0, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(bit1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(bit2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(bit3, GPIO.OUT, initial=GPIO.LOW)

# on and off
states = GPIO.LOW, GPIO.HIGH

def run_counter():

        for b3_val in states:
                for b2_val in states:
                        for b1_val in states:
                                for b0_val in states:
                                        GPIO.output(bit0, b0_val)
                                        GPIO.output(bit1, b1_val)
                                        GPIO.output(bit2, b2_val)
                                        GPIO.output(bit3, b3_val)
                                        sleep(2)



for _ in range(10):

	run_counter()

GPIO.cleanup()
