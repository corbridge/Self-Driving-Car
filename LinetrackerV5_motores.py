import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret: break # break if no next frame
    
    # Threshold
    lower = np.array([0, 0, 0])
    higher = np.array([50, 50, 50])
    mask = cv2.inRange(frame, lower, higher)

    # Detectando la línea
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, [255,0,0], 10)

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
    x_offset = cx - cx_cam
    x_centered = int(ancho/2) + x_offset
    cv2.circle(frame, (cx, cy),15 , (255, 255, 0), -1)

    # Calculando distancia del centro de la camara hacia la línea
    distancia = cx - cx_cam
    cv2.putText(frame, f"Distancia: {distancia} px", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Muestra el video en pantalla
    cv2.imshow('Frame', frame)
    cv2.imshow("Mask", mask)

    # Salir del bucle while
    if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
        break
        
cap.release()
cv2.destroyAllWindows()
