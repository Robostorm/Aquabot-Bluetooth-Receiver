import pygameController
import config
import RPi.GPIO as GPIO
from time import sleep

controller = pygameController.inputs

# Set Pins
aliePin = 2
elevPin = 3
buttonPin = 4

# Set pin order used in program
GPIO.setmode(GPIO.BCM)

# Pin Setup
GPIO.setup(aliePin, GPIO.OUT)
GPIO.setup(elevPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.OUT)

# PWM Setup
alie = GPIO.PWM(aliePin, 50)
elev = GPIO.PWM(elevPin, 50)

# PWM Initialization
alie.start(2.5)
elev.start(2.5)

# Main loop
while True:
    pygameController.getInputs()
    if controller.a:
        GPIO.output(buttonPin, GPIO.high)
    else:
        GPIO.output(buttonPin, GPIO.low)