import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, flipType=False)    # With Draw
    # hand = detector.findHands(img, draw=False) # No Draw
    cv2.imshow("Image", img)
    cv2.waitKey(1)
