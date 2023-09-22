#Logging Ultrasonic sensor values to firebase database
import time
import firebase_admin
import.GPIO as GPIO
from firebase.admin import credentials
from firebase_admin import db

trigPin=15
echoPin=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin.OUT)
GPIO.setup(echoPin,GPIO.IN)

def distance():
  GPIO.output(trigPin,True)
  time.sleep(0.00001)
  GPIO.output(trigPin,False)
  while GPIO.input(echoPin)==0:
    pulse_start=time.time()
  try:
    pulse_duration=pulse_end-pulse_start
  except:
    print("Calibrating")
    return 2000
  distance=pulse_duration*17150
  distance=round(distance+1.15,2)
  return distance

#Fetch the service account key JSON file contents
cred=credentials.Certificate('credentials.json')
#Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://iotif-manual.firebaseio.com'
})
#As an admin, the app has access to read and write all data,regardless of security
ref=db.reference('/')
distance_ref=ref.child('distance')
while True:
  try:
    distance_ref.push(distance())
    print(ref.get())
    time.sleep(5)
  except KeyboardInterrupt:
    print("\nExiting the program\n")
    GPIO.cleanup()
    exit()
