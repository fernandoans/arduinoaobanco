#include "dht.h" // BIBLIOTECA

#define PDHT11 A0
#define LDR A1

dht DHT;

int lums = 0;
float tensao;
float grauC;
float grauF;

void setup() {
  Serial.begin(9600);
}

void loop() {
  lums = analogRead(LDR);
  DHT.read11(PDHT11);
  grauC = DHT.temperature;
  grauF = grauC * (9.0/5.0) + 32.0;
  Serial.println(String(lums) + ":" + String(grauC) + 
       ":" + String(grauF) + ":" + String(DHT.humidity));
  delay(5000);
}
