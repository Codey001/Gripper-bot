#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

const int analogPin = A0;  // Change this to the analog pin where your sensor is connected

int analogValue = 0;

void setup() {
  Serial.begin(9600);

  // if(!display.begin(0x3c, Wire)) {
  //   Serial.println(F("SSD1306 allocation failed"));
  //   for(;;);
  // }

  display.display(); // Clear the display buffer
  delay(2000);  // Pause for 2 seconds
  display.clearDisplay();
}

void loop() {
  analogValue = analogRead(analogPin);
  

  display.clearDisplay();

  // Print the analog value on the OLED display
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 10);
  display.print(F("Analog Value:"));
  display.setCursor(0, 30);
  display.print(analogValue);

  // Update the display
  display.display();

  // Print the analog value to the serial monitor
  Serial.println(analogValue);

  delay(100);  // Adjust the delay as needed
}
