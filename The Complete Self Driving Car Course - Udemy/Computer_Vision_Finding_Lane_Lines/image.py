import cv2
import numpy as np

image = cv2.imread(r"C:\Users\DELL\Desktop\Cursos\The self driving car course\The-Complete-Self-Driving-Car-Course\The Complete Self Driving Car Course - Udemy\Computer_Vision_Finding_Lane_Lines\Image\test_image.jpg")
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,5),0)
canny = cv2.Canny(blur, 50, 150)

cv2.imshow('Result', canny)
cv2.waitKey(0)

