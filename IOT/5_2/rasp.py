#Raspberry Pi-Arduino Joystick Servo Motor Controller

#import the required i2c library
import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

servoPin=24
GPIO.setup(servoPin,GPIO.OUT)
p=GPIO.PWM(servoPin,50)
p.start(7.5)
bus=smbus.SMBus(1)

#This is the address we setup in the Arduino Program
address=0X04
while True:
  #Request the arduino for data
  data=bus.read_byte(address)
  #Print the data received from the arduino
  print(data)
  #20.4 Division Factor for mapping Joystick Output to Servo Position
  p.ChangeDutyCycle(data/20.4)
  time.sleep(1)
