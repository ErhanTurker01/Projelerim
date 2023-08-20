#include <Keypad.h>

int atoi(char key){
  return key - '1' + 1;
}

bool isNumber(char c){
  return c <= '9' && c >= '0';
}
enum color{
  red,
  green
};
void controlLED(int led, int color, int mode){
  if (color == red){
    digitalWrite(A3-led+1,mode);
  }
  else{
    digitalWrite(14-led,mode);
  }
}

int password = 1960;
const uint8_t ROWS = 4;
const uint8_t COLS = 4;
char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

uint8_t colPins[COLS] = { 5, 4, 3, 2 };
uint8_t rowPins[ROWS] = { 9, 8, 7, 6 };

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  for(int i=13;i>9;i--) pinMode(i, OUTPUT);
  for(int i=0;i<4;i++) pinMode(A3+i, OUTPUT);
  pinMode(A4, INPUT);
  Serial.begin(9600);
}

void loop() {
  for(int i=1;i<5;i++) controlLED(i,red,LOW);
  for(int i=1;i<5;i++) controlLED(i,green,LOW);

  int pass = 0;
  for(int i=1;i<5;i++){
    char key = keypad.waitForKey();
    if(!isNumber(key)){
      if(key == '*'){//Basılan tuşu geri alma
        controlLED(--i,green,LOW);
        controlLED(i--,red,LOW);
        pass/=10;
        continue;
      }
      i-=1;
      continue;
    }
    pass*=10;
    pass+=atoi(key);
    controlLED(i,green,HIGH);
    controlLED(i,red,HIGH);
  }

  if(pass != password){
    for(int i=1;i<5;i++) controlLED(i,green,LOW);
    for(int i=0;i<3;i++){
      for(int i=1;i<5;i++) controlLED(i,red,HIGH);
      delay(200);
      for(int i=1;i<5;i++) controlLED(i,red,LOW);
      delay(200);
    }
    
  }
  else{
    for(int i=1;i<5;i++) controlLED(i,red,LOW);
    while(true){
      int pot = analogRead(A4);
      Serial.println(pot);
      char key = keypad.getKey();
      if(key == '#'){//tekrar kilitle
        break;
      }
      if(key == '*'){//şifre değiştirme
        password = 0;
        for(int i=1;i<5;i++) controlLED(i,green,LOW);
        for(int i=1;i<5;i++) {
          key = keypad.waitForKey();
          if(!isNumber(key)){
            i--;
            continue;
          }
          password*=10;
          password+=atoi(key);
          controlLED(i,green,HIGH);
        }
        break;
      }
    }
  }
}