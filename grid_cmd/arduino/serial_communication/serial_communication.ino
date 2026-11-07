void setup() {
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    float elbowValue = Serial.parseFloat();
    float shoulderValue = Serial.parseFloat();
    
    Serial.print("Empfangen: ");
    Serial.print(elbowValue);
    Serial.print(", ");
    Serial.println(shoulderValue);
    
    while (Serial.available() > 0) {
      Serial.read();
    }
  }
}
