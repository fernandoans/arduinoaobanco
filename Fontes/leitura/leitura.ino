// C++ code
//
#define LDR A0
#define TMP335 A1

int lums = 0;
float tensao;
float grauC;
float grauF;

void setup() {
  pinMode(LDR, INPUT);
  pinMode(TMP335, INPUT);
  Serial.begin(9600); // bounds
}

void loop() {
  lums = map(analogRead(LDR), 244, 1100, 0, 100);
  tensao = (float(analogRead(TMP335)*5)/1024); // 5V e Leitura Analógica 0 a 1023 -> 1024
  grauC = tensao/ 0.010; // 0,010 mV
  grauF = grauC * (9.0/5.0) + 32.0;
  
  // {"lums": 99, "grauC": 24.3, "grauF": 78.3} 
  
  Serial.println("{\"lums\":" + String(lums) + ", \"grauC\":" + String(grauC) + ", \"grauF\":" + String(grauF) + "}");
  delay(2000);
}
