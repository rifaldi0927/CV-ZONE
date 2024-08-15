import cv2
import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8,maxHands=2)
myserial = cvzone.SerialModule.SerialObject("COM3", 9600,1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img) #With Draw
    #hands = detector.findHands(img, draw=False)#No Draw
    #print(len(hands))
    #Hand - dict (lmList - bbox - center - type)

    if hands:
        # Hand1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #List of 21 Landmark point
        bbox1 = hand1["bbox"] # Bounding box info x,y,w,h
        centerPoint1 = hand1["center"] # center of the hand cx,cy
        handType1 = hand1["type"] # Hand Type Left or Right
        fingers1 = detector.fingersUp(hand1)


        #print(len(lmList1),lmList1)
        #print(bbox1)
        #print(centerPoint1)
        #print(handType1)
        #print(fingers1)
        myserial.sendData(fingers1)

    cv2.imshow("image", img)
    cv2.waitKey(1)