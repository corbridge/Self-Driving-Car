from typing import ItemsView
import cv2
import numpy as np 
import threading
import RPi.GPIO as GPIO
import time

curva = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


R_EN = 21
L_EN = 22
RPWM = 23
LPWM = 24

AC = 13

GPIO.setup(AC, GPIO.IN)

GPIO.setup(R_EN, GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.output(R_EN, GPIO.HIGH)
GPIO.output(L_EN, GPIO.HIGH)

GPIO.setup(17,GPIO.OUT)
servo1 = GPIO.PWM(17,50)

my_pwm = GPIO.PWM(RPWM,100)
my_pwm1 = GPIO.PWM(LPWM,100)

servo1.start(0)
my_pwm.start(50)
my_pwm1.start(50)

def neutral():
    my_pwm.ChangeDutyCycle(0)
    my_pwm1.ChangeDutyCycle(0)

def back():
    my_pwm.ChangeDutyCycle(25)
    my_pwm1.ChangeDutyCycle(0)

def foward():
    my_pwm.ChangeDutyCycle(0)
    my_pwm1.ChangeDutyCycle(30)

def izquierda():
    servo1.ChangeDutyCycle(6.15)
    time.sleep(0.010)
    servo1.ChangeDutyCycle(0)


def derecha():
    servo1.ChangeDutyCycle(8.15)
    time.sleep(0.010)
    servo1.ChangeDutyCycle(0)


def derade():
    servo1.ChangeDutyCycle(6.35)
    time.sleep(0.010)
    servo1.ChangeDutyCycle(0)

def izqade():
    servo1.ChangeDutyCycle(7.65)
    time.sleep(0.010)
    servo1.ChangeDutyCycle(0)
    

def getLaneCurve(img):
        imgCopy = img.copy()
        
    #### STEP 1
        imgThres = thresholding(img)

    #### STEP 2
        h,w,c = img.shape 
        points = valTrackbars()

        imgWarp = warpImg(imgThres,points,w,h)
        imgWarpPoints = drawPoints(imgCopy,points)

    #### STEP 3
        midPoint, imgHist =  getHistogram(imgWarp, display = True, minPer=0.5,region =4)
        basePoint, imgHist = getHistogram(imgWarp, display = True, minPer=0.9)
        global curva
        curva = basePoint- midPoint

        #cv2.imshow('Thres',imgThres)
        cv2.imshow('Warp',imgWarp)
        cv2.imshow('Warp Points',imgWarpPoints)
        cv2.imshow('Histogram',imgHist)
        return None

        
  
    

def thresholding(img):
        imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lowerWhite = np.array([0,0,0])
        upperWhite = np.array([255,255,125])
        maskWhite = cv2.inRange(imgHsv,lowerWhite,upperWhite)
        return maskWhite 



def warpImg(img,points,w,h,):
     pts1 = np.float32(points)
     pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
     matrix = cv2.getPerspectiveTransform(pts1,pts2)
     imgWarp = cv2.warpPerspective(img,matrix,(w,h))
     return imgWarp

    

def initializeTrackbars(initialTracbarVals,wT = 480, hT=240):
        cv2.namedWindow("Trackbars")
        cv2.resizeWindow("Trackbars", 360,240)
        cv2.createTrackbar("Width Top", "Trackbars", initialTracbarVals[0],wT//2, nothing)
        cv2.createTrackbar("Height Top", "Trackbars", initialTracbarVals[1],hT, nothing)
        cv2.createTrackbar("Width Bottom", "Trackbars", initialTracbarVals[2],wT//2, nothing)
        cv2.createTrackbar("Height Bottom", "Trackbars", initialTracbarVals[3],hT, nothing)
    
    
def nothing(a):
    pass

def valTrackbars(wT=480, hT=240):
        widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
        heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
        widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
        heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
        points = np.float32([(widthTop, heightTop),(wT-widthTop, heightTop),
                       (widthBottom, heightBottom),(wT-widthBottom, heightBottom)])
    
    
        return points

 

def drawPoints (img,points):
        for x in range(4):
            cv2.circle(img,(int(points[x][0]),int (points[x][1])), 15,(0,0,255),cv2.FILLED)
        

        return img

def getHistogram(img, minPer = 0.1, display = False, region = 1):

    if region ==1:
        histValues = np.sum(img, axis = 0)
    else:
        histValues = np.sum(img[img.shape[0]//region:,:], axis = 0)

    #print(histValues) 
    maxValue = np.max(histValues)
    minValue = minPer*maxValue

    indexArray = np.where(histValues >= minValue)
    basePoint = int(np.average(indexArray))
    #print(basePoint)

    if display:
        imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
        for x, intensity in enumerate(histValues):
            cv2.line(imgHist,(x,img.shape[0]),(x,img.shape[0]-intensity//255//region),(255,0,255),1)
            cv2.circle(imgHist,(basePoint, img.shape[0]),20,(0,255,255),cv2.FILLED)
        return basePoint, imgHist
    
    return basePoint





t1 = threading.Thread(name="hilo 1",target = getLaneCurve, args=(1,))
t2 = threading.Thread(name="hilo 2",target = thresholding, args=(1,))
t3 = threading.Thread(name="hilo 3",target = warpImg, args=(1,))
t4 = threading.Thread(name="hilo 4",target = initializeTrackbars, args=(1,))
t5 = threading.Thread(name="hilo 5",target = valTrackbars, args=(1,))
t6 = threading.Thread(name="hilo 6",target = drawPoints, args=(1,))
t7 = threading.Thread(name="hilo 7",target = getHistogram, args=(1,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    intialTrackbarsVals = [130,65,5,240]
    initializeTrackbars(intialTrackbarsVals)
    frameCounter = 0
    
    
    #while True:
        
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter = 0
    
    while True:
        frameCounter += 1
        
        
        success, img = cap.read()
        img = cv2.resize(img,(480,240)) 
        getLaneCurve(img)
        print(curva)
        #cv2.imshow('vid', img) 
        cv2.waitKey(1)
        
        i = GPIO.input(AC)
    
        if i == 0:
            foward()
        elif i == 1:
            neutral()
        
        if curva < -40:
            izquierda()
            #print("izquierda")
        elif curva > 30:
            derecha()
            #print("derecha")
        elif curva > -40 and curva < -5:
            izqade()
            #print("adelante")
        elif curva > -5 and curva < 50:
            derade()
            #print("adelante")

GPIO.cleanup()