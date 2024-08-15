import pyfirmata
from pyfirmata import Arduino,SERVO,util
from time import sleep

comport='COM3'
pin = 12


board=Arduino(comport)
board.digital[pin].mode=SERVO


def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)



def led(total):
    if total == 0:
        # Rotate the servo to 10 degrees
        rotateservo(pin, 0)
        # Wait for a short time to let the servo reach the desired angle
        sleep(0.5)
        # Stop the servo by setting it to 0 degrees
        #rotateservo(pin, 0)
    elif total == 1:
        # Rotate the servo to 30 degrees
        rotateservo(pin, 0)
        sleep(0.5)
        #rotateservo(pin, 0)
    elif total == 2:
        # Rotate the servo to 60 degrees
        rotateservo(pin, 0)
        sleep(0.5)
        #rotateservo(pin, 0)
    elif total == 3:
        # Rotate the servo to 90 degrees
        rotateservo(pin, 0)
        sleep(0.5)
        #rotateservo(pin, 0)
    elif total == 4:
        # Rotate the servo to 120 degrees
        rotateservo(pin, 0)
        sleep(0.5)
        #rotateservo(pin, 0)
    elif total == 5:
        # Rotate the servo to 180 degrees
        rotateservo(pin, 180)
        sleep(0.5)
        #rotateservo(pin, 180)