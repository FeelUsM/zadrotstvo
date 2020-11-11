/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Blink
*/

#define INPIN 6
#define OUTPIN 5

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(OUTPIN, OUTPUT);
  pinMode(INPIN, INPUT);
}

bool foo(){

}
char s[32767];

int * p;

// the loop function runs over and over again forever
void loop() {
  for(int i=0; i<256; i+=32){
    analogWrite(OUTPIN,i);
    for(int j=0; j<5; j++){
      digitalWrite(LED_BUILTIN,digitalRead(INPIN));
      delay(100);
    }
  }
  for(int i=255; i>=0; i-=32){
    analogWrite(OUTPIN,i);
    for(int j=0; j<5; j++){
      digitalWrite(LED_BUILTIN,digitalRead(INPIN));
      delay(100);
    }
  }
}
