import cv2 as cv
import mediapipe as mp
import time


#Capturing video input from video capture device ( 0 )
cap = cv.VideoCapture(0)


#using the mediapipe framework
#specifically using the hand tracking trained model solution
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


pTime = 0
cTime = 0



while True:
    success, img = cap.read()
    imgFlip = cv.flip(img, 1)

    imgRGB = cv.cvtColor(imgFlip, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks :
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c=imgFlip.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cy, cx)

                # if id == 4:
                    # cv.circle(imgFlip, (cx, cy), 15, (255, 0, 255), cv.FILLED)

            mpDraw.draw_landmarks(imgFlip, handLms, mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(imgFlip, str(int(fps)), (10,70), cv.FONT_HERSHEY_TRIPLEX, 3, (255,0,255),thickness=2)

    cv.imshow("Image", imgFlip)
    cv.waitKey(1)
