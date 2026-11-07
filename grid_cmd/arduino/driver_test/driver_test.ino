#include <TMCStepper.h>

TMC2209Stepper driver(&Serial1, 0.11f, 0);

void setup() {
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);

  Serial.begin(115200);
  while (!Serial);

  Serial1.begin(115200);
  driver.begin();
}

void loop() {
  uint8_t result = driver.test_connection();

  if (result == 0) {
    Serial.println("OK");
  } else {
    Serial.println("FAILED");
  }
  delay(2000);
}
