/*
 * Author : Kunchala Anil
 * email : anilkuchalaece@gmail.com
 * 
 * This will ON and Off led and control the servoposition based on the commands from Python
 * And send the potentiometer data to the Python
 * 
 */
#include<Servo.h>

char startingChar = '!';
char endingChar = '@';
boolean storeData = false;
boolean commandRecv = false;
char dataRecv[20];
int dataIndex = 0;

Servo myServo;

void setup() {
  Serial.begin(115200);
  Serial.println("Hi there");
  pinMode(13,OUTPUT);
  myServo.attach(9);
}//end of setup

void loop() {
  if(Serial.available()){
    processRecvChar(Serial.read());
  }//end of if

  if(commandRecv){
    commandRecv = false;
    Serial.println(dataRecv);
    if(dataRecv[0] == 'L'){
      digitalWrite(13,getNumber(dataRecv,sizeof(dataRecv)));
    }else if(dataRecv[0] == 'S'){
     int servoValue = getNumber(dataRecv,sizeof(dataRecv));
      for (int j=0; j < servoValue ; j++)
      {
      myServo.write(j);
      delay(2);
    }//end of for
    }//end of ifElse
  }
}//end of loop

void processRecvChar(char recvChar){
  if (recvChar == startingChar){
    storeData = true;
    dataIndex = 0;
  }else if (recvChar == endingChar){
    dataRecv[dataIndex] = NULL;
    storeData = false;
    commandRecv = true;
  }else{
    if(storeData == true){
      dataRecv[dataIndex] = recvChar;
      dataIndex = dataIndex + 1;
    }//end of if
  }//end of ifElse
}//end of processRecvChar

unsigned int getNumber(char* dataRecv,int dataSize){
  char number[10];
  int  numberIndex = 0;

  for (int i = 0; i < dataSize - 1 ; i++ )
  {
    if (isdigit(dataRecv[i])){
      number[numberIndex] = dataRecv[i];
      numberIndex = numberIndex + 1;
    }//end of if
  }//end of for

  number[++numberIndex] = NULL;
  Serial.println(number);
  return atoi(number);
}//end of getNumber Fcn

