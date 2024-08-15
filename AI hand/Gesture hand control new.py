import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=1, detectionCon=0.7)
#mySerial = cvzone.SerialObject("COME3", 9600, 1)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findHands(img)
    #if lmList:
        #fingers = detector.fingersUp()
        #   print(fingers)
        #mySerial.sendData(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
