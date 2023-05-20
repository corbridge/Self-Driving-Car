import cv2
import numpy as np
import requests
import keyboard

cap = cv2.VideoCapture("http://192.168.1.14:81/stream") 
comando=0

while True:
    ret, frame = cap.read()
    if not ret: break # break if no next frame

    # Filtrado del video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Detectando la línea
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 10)

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
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

    # Calculando distancia del centro de la camara hacia la línea
    distancia = cx - cx_cam
    cv2.putText(frame, f"Distancia: {distancia} px", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Muestra el video en pantalla
    cv2.imshow("IP VIDEO", frame)

    if keyboard.is_pressed("a"):
        comando=3
    if keyboard.is_pressed("s"):
        comando=0
    if keyboard.is_pressed("d"):
        comando=1
    if keyboard.is_pressed("x"):
        comando=4
    if keyboard.is_pressed("w"):
        comando=2
    

    # Envio de datos a la esp32
    datos = {
        "distancia": comando
    }
    response = requests.post("http://192.168.1.14:81", data = datos)
    """ if response.status_code == 200:
        print("Variable enviada")
    else:
        print("Error al enviar la variable") """
    
    # Salir del bucle while
    if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
        break
        
cap.release()
cv2.destroyAllWindows()