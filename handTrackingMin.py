import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks :
            mpDraw.draw_landmarks(img, handLms)


    cv.imshow("Image", img)
    cv.waitKey(1)
