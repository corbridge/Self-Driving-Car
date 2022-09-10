from pickletools import uint8
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
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):

    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(line_image, (x1,y1),(x2,y2), (0,255,0), 10)
    return line_image
        




