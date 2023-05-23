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
    GPIO.output(MotorIN2,GPIO.HIGH) # Establecemos el sentido de giro con los pines IN1 e IN2  
    GPIO.output(MotorIN4,GPIO.LOW)  # Establecemos el sentido de giro con los pines IN1 e IN2
    GPIO.output(MotorIN1,GPIO.HIGH)   # Establecemos el sentido de giro con los pines IN1 e IN2   
    GPIO.output(MotorIN3,GPIO.LOW) 

def backward():
    GPIO.output(MotorIN2,GPIO.LOW) # Establecemos el sentido de giro con los pines IN1 e IN2  
    GPIO.output(MotorIN4,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
    GPIO.output(MotorIN1,GPIO.LOW)   # Establecemos el sentido de giro con los pines IN1 e IN2   
    GPIO.output(MotorIN3,GPIO.HIGH) 

while True:
    foward()
    sleep(5)
    backward()
    sleep(5)

GPIO.cleanup()