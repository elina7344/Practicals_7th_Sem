#Connecting Relay to MQTT broker and controlling its ON and OFF
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


relayPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin , GPIO.OUT)


def on_connect(client , userdata , flags , rc):
    print("Connected with result code" , str(rc))
    client.subscribe("IOTIF/RPi")
    
    
def on_message(client , userdata , message):
    data = str(message.payload.decode("utf-8")).strip()
    print("Data received on topic:" , message.topic , " | Message: " , data)
    
    if data.upper() == "ON":
        GPIO.output(relayPin , True)
        print("Relay On")
    elif data.upper() == "OFF":
        GPIO.output(relayPin , False)
        print("Relay Off")
    else:
        print("Invalid command. Try sending ON or OFF")
        

client = mqtt.Client()
client.connect("broker.hivemq.com")

client.on_connect = on_connect
client.on_message = on_message

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nExiting the program\n")
    GPIO.cleanup()
    exit()
