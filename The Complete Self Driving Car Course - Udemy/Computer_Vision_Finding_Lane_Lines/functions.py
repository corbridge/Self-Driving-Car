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

    color = (0,255,0)
    thick = 10

    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(line_image, (x1,y1),(x2,y2), color, thick)
    return line_image

def average_slope_intercept(image, lines):
    
    left_fit = []
    right_fit = []

    for line in lines:
        x1,y1,x2,y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2), (y1,y2), 1)
        slope = parameters[0]
        intercept = parameters[1]

        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    left_fit_average = np.average(left_fit, axis = 0)
    right_fit_average = np.average(right_fit,  axis = 0)

    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])

def make_coordinates(image, line_parameters):

    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1 * (3/5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1,y1,x2,y2])
        




