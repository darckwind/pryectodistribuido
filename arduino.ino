#include <DHT11.h>


int pinRelay = 5;
int pin = 4;


DHT11 dht11(pin);

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pinRelay, OUTPUT);
  while (!Serial);
}

// the loop function runs over and over again forever
void loop() {


  if (Serial.available()){
      int state = Serial.parseInt();
      if (state == 1){
          digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on
          digitalWrite(pinRelay, HIGH);
        }
        if (state == 2){
          digitalWrite(LED_BUILTIN, LOW);   // turn the LED on
          digitalWrite(pinRelay, LOW);
        }
    }


  int err;
  float temp, humi;
  String dht11_final;
  if((err=dht11.read(humi, temp))==0)
  {
    dht11_final = String(humi)+"@"+String(temp);

  }
  else
  {
    dht11_final = String(000)+"@"+String(000);
  }
  delay(DHT11_RETRY_DELAY); //delay for reread


  int sensor_pt100 = random(1,455);



  String final_data = dht11_final +"@"+ String(sensor_pt100);
  Serial.println(final_data);

}