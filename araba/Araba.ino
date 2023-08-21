#define REMOTEXY_MODE__HARDSERIAL

#include <RemoteXY.h>

// RemoteXY connection settings 
#define REMOTEXY_SERIAL Serial
#define REMOTEXY_SERIAL_SPEED 9600


// RemoteXY configurate  
#pragma pack(push, 1)
uint8_t RemoteXY_CONF[] =   // 53 bytes
  { 255,6,0,0,0,46,0,16,25,0,5,32,1,20,41,41,77,25,31,5,
  32,57,20,42,42,77,25,31,4,128,7,6,90,5,77,26,10,49,90,12,
  9,9,77,26,31,79,78,0,31,79,70,70,0 };
  
// this structure defines all the variables and events of your control interface 
struct {

    // input variables
  int8_t joystick_1_x; // from -100 to 100  
  int8_t joystick_1_y; // from -100 to 100  
  int8_t yonj_x; // from -100 to 100  
  int8_t yonj_y; // from -100 to 100  
  int8_t maxh; // =0..100 slider position 
  uint8_t switch_1; // =1 if state is ON, else =0 

    // other variable
  uint8_t connect_flag;  // =1 if wire connected, else =0 

} RemoteXY;
#pragma pack(pop)

/////////////////////////////////////////////
//           END RemoteXY include          //
/////////////////////////////////////////////



void setup() 
{
  RemoteXY_Init (); 
    for(int i=3;i<=6;i++){
    pinMode(i,OUTPUT);
  }
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(31,OUTPUT);
}

void loop() 
{ 
  RemoteXY_Handler ();
 double hizsag,hizsol;
  hizsag=RemoteXY.joystick_1_y*2.55*RemoteXY.maxh/100;
  hizsol=RemoteXY.joystick_1_y*2.55*RemoteXY.maxh/100;

  if(RemoteXY.joystick_1_y>0){
    digitalWrite(12,LOW);
    if(RemoteXY.yonj_x>0){//sağ
      if(RemoteXY.yonj_x>50){//ters
        hizsag*=0.02*RemoteXY.yonj_x-1;
        digitalWrite(3,LOW);
        digitalWrite(4,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,LOW);
      }
      else{//yavaş
      hizsag*=-0.02*RemoteXY.yonj_x+1;
        digitalWrite(3,HIGH);
        digitalWrite(4,LOW);
        digitalWrite(5,HIGH);
        digitalWrite(6,LOW);
      }
    }
    else{//sol
      if(RemoteXY.yonj_x<-50){//ters
      hizsol*=-0.02*RemoteXY.yonj_x-1;
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
      }
      else{//yavaş
      hizsol*=0.02*RemoteXY.yonj_x+1;
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      }
    }
  }
  else if(RemoteXY.joystick_1_y<0){
    digitalWrite(12,HIGH);
    hizsag*=-1;
    hizsol*=-1;
    if(RemoteXY.yonj_x>0){//sağ
      if(RemoteXY.yonj_x>50){//ters
        hizsag*=0.02*RemoteXY.yonj_x-1;
        digitalWrite(4,LOW);
        digitalWrite(3,HIGH);
        digitalWrite(6,HIGH);
        digitalWrite(5,LOW);
      }
      else{//yavaş
      hizsag*=-0.02*RemoteXY.yonj_x+1;
        digitalWrite(4,HIGH);
        digitalWrite(3,LOW);
        digitalWrite(6,HIGH);
        digitalWrite(5,LOW);
      }
    }
    else{//sol
      if(RemoteXY.yonj_x<-50){//ters
      hizsol*=-0.02*RemoteXY.yonj_x-1;
      digitalWrite(4,HIGH);
      digitalWrite(3,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,HIGH);
      }
      else{//yavaş
      hizsol*=0.02*RemoteXY.yonj_x+1;
      digitalWrite(4,HIGH);
      digitalWrite(3,LOW);
      digitalWrite(6,HIGH);
      digitalWrite(5,LOW);
      }
    }
  }
  else{
    digitalWrite(12,LOW);
    if(RemoteXY.yonj_x>=0){
      hizsag=RemoteXY.yonj_x*2.55*RemoteXY.maxh/100;
      hizsol=RemoteXY.yonj_x*2.55*RemoteXY.maxh/100;
      digitalWrite(3,LOW);
      digitalWrite(4,HIGH);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
    }
    else{
      hizsag=-RemoteXY.yonj_x*2.55*RemoteXY.maxh/100;
      hizsol=-RemoteXY.yonj_x*2.55*RemoteXY.maxh/100;
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
    }
  }

  analogWrite(9,hizsag);
  analogWrite(10,hizsol); 
  if(RemoteXY.switch_1){
    digitalWrite(31,HIGH);
  }
  else{
    digitalWrite(31,LOW);
  }
}