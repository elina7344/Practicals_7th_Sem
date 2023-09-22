#Publishing the DHT sensor value to web page using MQTT
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from dht11 import DHT11
import time

publishTopic="IOTIF/RPI/DHT"
sensorPin=26
sensor=DHT11(pin=sensorPin)

def on_connect(client,userdata,flags,rc):
  print("Connected with result code",str(rc))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

client=mqtt.Client()
client.on_connect=on_connect

try:
  while True:
    result=sensor.read()
    if result.is_valid():
      humidity=round(result.humidity,2)
      temperature=round(result.temperature,2)
      print(f"Temperature: {temperature} C")
      print(f"Humidity: {humidity} %")
      msg=f"{humidity},{temerature}"
      client.publish(publishTopic,msg)
    client.loop()
    time.sleep(5)

except KeyboardInterrupt:
  print("\nExiting the program\n")
  GPIO.cleanup()
  exit()
