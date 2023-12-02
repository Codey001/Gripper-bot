const int ledPin = A0;  // Change this to the pin where your LED is connected

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
      Serial.println("LED is ON");
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Turn off the LED
      Serial.println("LED is OFF");
    }
  }
}
