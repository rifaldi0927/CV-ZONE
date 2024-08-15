import pyfirmata
from pyfirmata import Arduino,SERVO,util
from time import sleep

comport = 'COM3'
pins = [9, 10, 11, 12, 13]

board = Arduino(comport)

for pin in pins:
    board.digital[pin].mode=SERVO


def rotateservo(pin,angle):
        board.digital[pin].write(angle)
        sleep(0.005)# it make servo faster previus is 0.015


# Function to control the finger servos based on the finger states
def control_finger_servos(finger_states):
    if len(finger_states) != len(pins):
        print("Error: Number of finger states should match the number of servos.")
        return

    for i in range(len(pins)):
        if finger_states[i]:
            rotateservo(pins[i], 90)  # Move the servo to 90 degrees when the finger is up
        else:
            rotateservo(pins[i], 0)   # Move the servo to 0 degrees when the finger is down


# Example usage:
# Simulate 1 finger up and 4 fingers down
finger_states = [True, False, False, False, False]
control_finger_servos(finger_states)





def led(total):
    if total == 0:
        for i in range(0,180):
            for pin in pins:
                rotateservo(pin,i)
    elif total == 1:
        for i in range(0,90):
            for pin in pins:
                rotateservo(pin,i)

