#include<Servo.h>
int servoPin = 3;
//Servo object
Servo Servo1;

void setup(){
  Serial.begin(9600);
  //Attach servo to pin number
  Servo1.attach(servoPin);
}

void loop(){
  if(Serial.available()>0){
    String receivedString = Serial.readStringUntil('\n');

    if(receivedString.length()>0){
      int angle1 = receivedString.toInt();
      Servo1.write(angle1);
    }
  }
}