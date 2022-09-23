import cv2
import numpy as np
import matplotlib.pyplot as plt
from functions import *

image = cv2.imread(r"C:\Users\DELL\Desktop\Cursos\The self driving car course\The-Complete-Self-Driving-Car-Course\The Complete Self Driving Car Course - Udemy\Computer_Vision_Finding_Lane_Lines\Image\test_image.jpg")
edges = canny(image)
cropped_image = region_of_interest(edges)
line = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
average_line = average_slope_intercept(image, line)
line_image = display_lines(image, average_line)
merge_image = cv2.addWeighted(image, 0.8, line_image, 1,1)

cv2.imshow('Result', merge_image)
cv2.waitKey(0)

