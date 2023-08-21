#include <Wire.h>
#include <Servo.h>
#define trigPin 3
#define echoPin 4
Servo servo;

void mesafeOlcer(){
double sure, mesafe;
digitalWrite(trigPin, LOW);
delayMicroseconds(trigPin);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
sure = pulseIn(echoPin, HIGH);
mesafe = (sure/2) * 0.0343;
Serial.println(mesafe);
delay(100);
}

void setup () {
Serial.begin(9600);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
pinMode(A1,INPUT);
servo.attach(9);
}

void loop () {
  int x=analogRead(A1);
  x=map(x, 0, 655, 0, 180); 
  Serial.println(x);
  servo.write(x);
  delay(15);   
}