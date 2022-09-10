from email.mime import image
import cv2
import numpy as np
import matplotlib as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    triangule = np.array([(200, height),(1100, height), (550,250)], dtype=np.int64)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [triangule], 255)
    return mask
