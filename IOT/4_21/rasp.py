#Control LED brightness by sending PWM values using MQTT
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

ledPin=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
pwm=GPIO.PWM(ledPin,100)
pwm.start(0)

def on_connect(client,userdata,flags,rc):
  print("Connected with result code",str(rc))
  client.subscribe("IOTIF/RPi/PWM")

def on_message(client,userdata,message):
  data=str(message.payload.decode("utf-8")).strip()
  print("Data received on topic:",message.topic, " | Message:",data)
  pwm.ChangeDutyCycle(int(data))
client=mqtt.Client()
client.connect("broker.hivemq.com")
client.on_connect=on_connect
client.on_message=on_message
try:
  client.loop_forever()
except KeyboardInterrupt:
  print("\nExiting the program\n")
  GPIO.cleanup()
  exit()
