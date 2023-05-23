import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

MotorIN1 = 2
MotorIN2 = 3

MotorIN3 = 17
MotorIN4 = 27

GPIO.setup(MotorIN1,GPIO.OUT)
GPIO.setup(MotorIN2,GPIO.OUT)

GPIO.setup(MotorIN3,GPIO.OUT)
GPIO.setup(MotorIN4,GPIO.OUT)

print("Hacemos girar el motor en un sentido por 5 segundos")
GPIO.output(MotorIN1,GPIO.HIGH) # Establecemos el sentido de giro con los pines IN1 e IN2  
GPIO.output(MotorIN2,GPIO.LOW)  # Establecemos el sentido de giro con los pines IN1 e IN2

sleep(5)

print("Hacemos girar el motor en el sentido contrario por 5 segundos")
GPIO.output(MotorIN3,GPIO.LOW)   # Establecemos el sentido de giro con los pines IN1 e IN2   
GPIO.output(MotorIN4,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2 

sleep(5)

GPIO.cleanup()