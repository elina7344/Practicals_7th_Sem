//7 8 AN->DHT
//A4 A5 AN->LCD
#include<LiquidCrystal_I2C.h>
#include<DHT.h>
string tempMessage;
string humMessage;
void setup()
{
lcd.begin(16,2);
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print("DHT11 Sensor");
  dht.begin();
  Serial.begin(9600);
  Serial.println("Temperature and Humidity Sensor");
}

void loop()
{
float h = dht.readHumidity();
  float t = dht.readTemperature();
  if(isnan(h) || isnan(t))
  {
Serial.println("Failed to read from DHT sensor!")l
  loop();
  }
  tempMessage="Temp: "+String(t)+"C";
  humMessage="Hum: "+String(h)+"%";
  Serial.println(tempMessage+ "     ");
  Serial.println(humMessage);
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print(tempMessage);
  lcd.setCursor(1,1);
  lcd.print(humMessage);
  delay(1000);
}
