import pygameController
from gpiozero import OutputDevice, Servo
from time import sleep

controller = pygameController.inputs

# Configure Pins
alie = Servo(2)
elev = Servo(3)
button = OutputDevice(4)

# Main loop
while True:
    pygameController.getInputs()
    if controller.a:
        OutputDevice.on()
    else:
        OutputDevice.off()

    alie.value = (controller.right_stick_x + 1) / 2
    elev.value = (controller.right_stick_y + 1) / 2