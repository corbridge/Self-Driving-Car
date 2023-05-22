import cv2
import numpy as np

def get_error(frame):
    frame = cv2.GaussianBlur(frame, (5,5), 0)

    # Threshold
    lower = np.array([0, 0, 0])
    higher = np.array([80, 80, 80])
    mask = cv2.inRange(frame, lower, higher)

    # Detectando la línea
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrando el punto medio de la línea
    biggest_contour = max(contours, key = cv2.contourArea)
    M = cv2.moments(biggest_contour)

    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    ancho = frame.shape[1]
    cx_cam = int(ancho/2)

    # Calculando distancia del centro de la camara hacia la línea
    distancia = cx - cx_cam

    return distancia