import cv2

image = cv2.imread(r"C:\Users\DELL\Desktop\Cursos\The self driving car course\The-Complete-Self-Driving-Car-Course\The Complete Self Driving Car Course - Udemy\Computer_Vision_Finding_Lane_Lines\Image\test_image.jpg")
cv2.imshow('Result', image)
cv2.waitKey(0)