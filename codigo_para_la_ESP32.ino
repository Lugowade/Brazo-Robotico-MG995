#include <ESP32Servo.h>

#define NUM_SERVOS 6
const int servoPins[NUM_SERVOS] = {13, 12, 33, 27, 26, 25};

Servo servos[NUM_SERVOS];
String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(115200);
  delay(1000);

  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].setPeriodHertz(50);
    servos[i].attach(servoPins[i], 600, 2400);
    servos[i].write(90);
    delay(100);
  }
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
      break;
    } else {
      inputString += inChar;
    }
  }

  if (stringComplete) {
    processCommand(inputString);
    inputString = "";
    stringComplete = false;
  }
}

void processCommand(String cmd) {
  cmd.trim();
  if (!cmd.startsWith("S")) return;

  int colonIndex = cmd.indexOf(':');
  if (colonIndex == -1) return;

  int servoIndex = cmd.substring(1, colonIndex).toInt();
  int angle = cmd.substring(colonIndex + 1).toInt();

  if (servoIndex >= 0 && servoIndex < NUM_SERVOS && angle >= 0 && angle <= 180) {
    servos[servoIndex].write(angle);
  }

  delay(2);
}
