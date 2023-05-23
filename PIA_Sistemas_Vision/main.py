import cv2
import numpy as np
import lineTrackerAlgorithm
import motors

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret: break # break if no next frame
    distancia = lineTrackerAlgorithm.distance_from_center(frame)

    if distancia >= -10 and distancia <= 10:
        motors.foward()
    elif distancia > -10:
        motors.right()
    elif distancia < 10:
        motors.left()