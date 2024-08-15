import pyfirmata
from pyfirmata import Arduino,SERVO,util
from time import sleep

comport='COM3'
pin = 10


board=Arduino(comport)
board.digital[pin].mode=SERVO


def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)


def led(total):
    if total == 0:
        for i in range(0,180):
            rotateservo(pin,i)
    elif total == 1:
        for i in range(0,90):
            rotateservo(pin,i)