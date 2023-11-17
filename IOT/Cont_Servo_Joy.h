//12 13 AN->Servo
//8 pin to joystick
#include<Servo.h>
Servo myservo;
int servoPin=12;
int joyX=A1;
int xPos;

void setup()
{
pinMode(joyX,INPUT);
  myservo.attach(servoPin);
  Serial.begin(9600);
  Serial.println("Move the Joystick up and down");
  
}

void loop()
{
xPos=analogRead(joyX);
  if(xPos>300 && xPos<700)
  {
myservo.write(90);
    delay(15);
  }
  else if(xPos<300)
  {
myservo.write(0);
    delay(15);
  }
  else if(xPos>700)
  {
myservo.write(80);
    delay(15);
  }
}
