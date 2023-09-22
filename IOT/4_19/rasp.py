import RPi.GPIO as GPIO
import time

def ledPatternOne():
  for i in range(10,14):
    GPIO.output(i,GPIO.HIGH)
    time.sleep(1)
  for i in range(10,14):
    GPIO.output(i,GPIO.LOW)
    time.sleep(1)
    
def ledPatternTwo():
  for i in range(10,14):
    GPIO.output(i,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(i,GPIO.LOW)
    time.sleep(1)

def ledPatternThree():
  for i in range(13,9,-1):
    GPIO.output(i,GPIO.HIGH)
    time.sleep(1)
  for i in range(13,9,-1):
    GPIO.output(i,GPIO.LOW)
    time.sleep(1)

def ledPatternFour():
  for i in range(10,14,2):
    GPIO.output(i,GPIO.HIGH)
    time.sleep(1)
  for i in range(11,14,2):
    GPIO.output(i,GPIO.HIGH)
    time.sleep(1)
  for i in range(10,14,2):
    GPIO.output(i,GPIO.LOW)
    time.sleep(1)
  for i in range(11,14,2):
    GPIO.output(i,GPIO.LOW)
    time.sleep(1)

def main():
  GPIO.setmode(GPIO.BCM)
  for i in range(10,14):
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)
  try:
    while True:
      n=input("Enter 1/2/3/4 for different LED patterns: ")
      if n=='1':
        ledPatternOne()
      elif n=='2':
        ledPatternTwo()
      elif n=='3':
        ledPatternThree()
      elif n=='4':
        ledPatternFour()
      else:
        print("Invalid Entry")

   except KeyboardInterrupt:
     print("\nExiting the program\n")
     GPIO.cleanup()
     exit()

main()


