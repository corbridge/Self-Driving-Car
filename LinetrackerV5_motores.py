import cv2

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret: break # break if no next frame

    # Filtrado del video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(gray_blur, 150, 255, cv2.THRESH_BINARY_INV)

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
    cv2.circle(frame, (cx, cy),15 , (255, 255, 0), -1)

    # Calculando distancia del centro de la camara hacia la línea
    distancia = cx - cx_cam
    cv2.putText(frame, f"Distancia: {distancia} px", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Muestra el video en pantalla
    cv2.imshow('frame', frame)
    cv2.imshow("THRESH", thresh)

    # Salir del bucle while
    if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
        break
        
cap.release()
cv2.destroyAllWindows()

for key, value in M.items():
        print(f'{key}: {value}')