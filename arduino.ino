#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

int pinRelay = 3;

#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

int pinRelay = 3;

const int analogInPin = A0;
int sensorValue = 0;


void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pinRelay, OUTPUT);
  while (!Serial);
  dht.begin();
}

void loop() {
    if (Serial.available()){
      int state = Serial.parseInt();
      if (state == 1){
          digitalWrite(LED_BUILTIN, HIGH);   // turn the actuador on
          digitalWrite(pinRelay, HIGH);
        }
        if (state == 2){
          digitalWrite(LED_BUILTIN, LOW);   // turn the actuador on
          digitalWrite(pinRelay, LOW);
        }
    }


  sensorValue = analogRead(analogInPin);
  float temp_analog = (1.3125*(sensorValue-428)+3.3);
  float temp, humi;
  String dht11_final;
  humi = dht.readHumidity();
  temp = dht.readTemperature();
  dht11_final = String(humi)+"@"+String(temp);
  String final_data = dht11_final +"@"+ String(temp_analog);
  Serial.println(final_data);
  delay(1000);

}