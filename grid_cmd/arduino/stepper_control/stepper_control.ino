#include <TMCStepper.h>
#include <AccelStepper.h>

#define STEP_PIN 4
#define DIR_PIN 3
#define EN_PIN 2

TMC2209Stepper driver(&Serial1, 0.11f, 0b00);

AccelStepper stepper(1, STEP_PIN, DIR_PIN);

const float STEPS_PER_TURN = 6400.0;
const float STEPS_PER_DEGREE = STEPS_PER_TURN / 360;

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  pinMode(EN_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  digitalWrite(EN_PIN, HIGH);  

  Serial.begin(9600);
  Serial.setTimeout(50);
  Serial1.begin(115200);

  driver.begin();

  while (driver.test_connection() != 0) {
    digitalWrite(LED_BUILTIN, HIGH);  
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);  
    delay(500);

    Serial.print("Driver: ");
    Serial.println(driver.test_connection());
  }
  digitalWrite(LED_BUILTIN, LOW);

  driver.begin();                      
  driver.I_scale_analog(false);       
  driver.rms_current(600);             
  driver.microsteps(16);

  stepper.setMaxSpeed(4000);
  stepper.setAcceleration(2000);
  stepper.setCurrentPosition(0);

  digitalWrite(EN_PIN, LOW);          
}

void loop() {
  stepper.run();

  if (Serial.available() > 0) {
    float steps_elbow = Serial.parseFloat();
    float steps_shoulder = Serial.parseFloat();
    
    Serial.print(steps_elbow);
    Serial.print(", ");
    Serial.println(steps_shoulder); 

    stepper.moveTo(steps_elbow);

    while (Serial.available() > 0) {
      Serial.read();
    }
  }
}