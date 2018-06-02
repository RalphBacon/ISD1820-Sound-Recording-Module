/*
 * Simple circuit to test the triggering of the IDS1820 Voice Recording Module
 * 
 * Connect VCC to the 3.3V of the Arduino Uno/Nano etc
 * Connect GND to a spare GND pin on your Arduino
 * Connect P-E (pulse edge) pin of the IDS1820 to pin 2 of the Arduino
 * Ensure you have removed the jumper from P-E on the module
 */

#define triggerPin 2

void setup() {

  Serial.begin(9600);

  // Set the trigger pin in this sequence to prevent false triggering on start
  digitalWrite(triggerPin, LOW);
  pinMode(triggerPin, OUTPUT);  
  
  Serial.println("Start up completed");
}

void loop() {

  digitalWrite(triggerPin, HIGH);
  delay(100);
  digitalWrite(triggerPin, LOW);
  delay(10000);  
}
