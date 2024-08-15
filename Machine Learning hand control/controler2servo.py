import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep

comport = 'COM3'
pins = [13, 12]  # Pins for two servos (two fingers)

board = Arduino(comport)

# Initialize servos and set their modes
for pin in pins:
    board.digital[pin].mode=SERVO
#servos = [board.digital[pin].mode(SERVO) for pin in pins]

# Function to rotate a servo to a given angle
def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

# Function to control the fingers

def led(total):
    if total == 0:
        # Rotate the servo to 10 degrees
        rotateservo(pins[0],180)
        rotateservo(pins[1],0)
        # Wait for a short time to let the servo reach the desired angle
        sleep(0.5)
        # Stop the servo by setting it to 0 degrees
        #rotateservo(pin, 0)
    elif total == 1:
        # Rotate the servo to 30 degrees
        rotateservo(pins[0],0)
        rotateservo(pins[1],0)
        sleep(0.5)
        #rotateservo(pin, 0)
    elif total == 2:
        # Rotate the servo to 60 degrees
        rotateservo(pins[0],0)
        rotateservo(pins[1],180)
        sleep(0.5)
        #rotateservo(pin, 0)
