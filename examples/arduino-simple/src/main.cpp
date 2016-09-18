#include <Arduino.h>

void setup() {
  SerialUSB.begin(115200);
  SerialUSB.println("Batman");
}

void loop() {
  SerialUSB.print("nananana");
}
