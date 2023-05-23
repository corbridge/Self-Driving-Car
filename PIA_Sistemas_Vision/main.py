import cv2
import numpy as np
import lineTrackerAlgorithm
import motors
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret: break
    distancia = lineTrackerAlgorithm.distance_from_center(frame)

    if distancia >= -10 and distancia <= 10:
        motors.foward()
    elif distancia > -10:
        motors.right()
    elif distancia < 10:
        motors.left()
GPIO.cleanup()