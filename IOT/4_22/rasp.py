import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import RPi_I2C_driver
mylcd=RPi_I2C_driver.lcd(0x38)
mylcd.backlight(1)
mylcd.lcd_clear()

def on_connect(client,userdata,flags,rc):
    print("Connected with results code",str(rc))
    client.subscribe("IOTIF/RPI/LCD")
    
def on_message(client,userdata,message):
    data=str(message.payload.decode("utf-8")).strip()
    print("Data received on topic:",message.topic,"| Message:",data)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Data:"+data,1)
    
client =mqtt.client()
client.connect("broker.hivemq.com")
client.on_message=on_message

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nExiting the program\n")
    GPIO.cleanup()
    exit()
