//Import the library
#include<Wire.h>
int joyY=A0;
//SECONDARY Address for the Communication
#define SECONDARY_ADDRESS 0x04

//Code Initialization
void setup()
{
  Serial.begin(9600);
  Wire.begin(SECONDARY_ADDRESS);
  Serial.println("I2C Begin");
}
void loop()
{
  Wire.onRequest(sendData);
  delay;
}
void sendData()
{
  Wire.write(analogRead(joyY));
  Serial.println("Joystick Value Sent");
}
