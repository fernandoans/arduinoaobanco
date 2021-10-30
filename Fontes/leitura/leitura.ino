#define LDR A0
#define LM35 A1

int lums = 0;
float tensao;
float grauC;
float grauF;

void setup() {
  pinMode(LDR, INPUT);
  pinMode(LM35, INPUT);
  Serial.begin(9600);
}

void loop() {
  lums = map(analogRead(LDR), 244, 1100, 0, 100);
  tensao = (float(analogRead(LM35))*5)/1023; // 5V e leitura analógica 0 a 1023
  grauC = tensao / 0.010; // 0,010 mV
  grauF = grauC * (9.0/5.0) + 32.0;
  Serial.println("{\"lums\":" + String(lums) + ", \"grauC\":" 
    + String(grauC) + ", \"grauF\":" + String(grauF) + "}"); 
  delay(5000); // 5 segundos
}
