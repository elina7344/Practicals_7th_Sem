// A4 A5 of AN->LCD
// 7 8 of AN -> US
// 10 11 of AN->buzzer
//12 13 of AN-> PIR
#include<NewPing.h>
#include<LiquidCrystal_I2C.h>
NewPing sonar(7,8,200);
LiquideCrystal_I2C(0x38,4,5,6,0,1,2,3,7,NEGATIVE);
int buzzerPin=10;
int pirPin=12;
const int distThresh=25;
void setup()
{
pinMode(buzzerPin,OUTPUT);
  pinMode(pirPin,INPUT);
  lcd.begin(16,2);
}
void loop()
{
int dist=sonar.ping_cm();
if(dist<distThresh || digitalRead(pirPin))
{
digitalwrite(buzzerPin,HIGH);
  lcd.home();
  lcd.print("Intruder detected");
  delay(2000);
}
  else
{
digitalWrite(buzzerPin,HIGH);
  lcd.home();
  lcd.print("No Intruder");
}
  delay(10);
}
