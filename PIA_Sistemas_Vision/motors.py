import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MotorIN1 = 12
MotorIN2 = 13
MotorIN3 = 18
MotorIN4 = 19

GPIO.setup(MotorIN1,GPIO.OUT)
GPIO.setup(MotorIN2,GPIO.OUT)
GPIO.setup(MotorIN3,GPIO.OUT)
GPIO.setup(MotorIN4,GPIO.OUT)

def foward():
    GPIO.output(MotorIN2,GPIO.HIGH)
    GPIO.output(MotorIN4,GPIO.LOW)

    GPIO.output(MotorIN1,GPIO.HIGH) 
    GPIO.output(MotorIN3,GPIO.LOW)

def backward():
    GPIO.output(MotorIN2,GPIO.LOW)
    GPIO.output(MotorIN4,GPIO.HIGH)

    GPIO.output(MotorIN1,GPIO.LOW)
    GPIO.output(MotorIN3,GPIO.HIGH)

def left():
    GPIO.output(MotorIN2,GPIO.LOW)
    GPIO.output(MotorIN4,GPIO.HIGH)

    GPIO.output(MotorIN1,GPIO.HIGH)
    GPIO.output(MotorIN3,GPIO.LOW)

def right():
    GPIO.output(MotorIN2,GPIO.HIGH)
    GPIO.output(MotorIN4,GPIO.LOW)

    GPIO.output(MotorIN1,GPIO.LOW)
    GPIO.output(MotorIN3,GPIO.HIGH)

while True:
    foward()
    print('ADELANTE')
    sleep(5)
    backward()
    print('ATRAS')
    sleep(5)
    right()
    print('DERECHA')
    sleep(5)
    left()
    print('IZQUIERDA')
    sleep(5)

GPIO.cleanup()