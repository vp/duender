///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//         Arduino code for setting servo (Hi-Tech 311) to the neutral position
//         See the following video on my channel "Let There Be Engineering" for more details:
//         https://youtu.be/9Hul2amhBSM "How to Set a Servo Motor to the Neutral Position using Arduino: A Step-by-Step Guide" 
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#include <Servo.h>

int pos;  // position of servo (range between 0 and 180; 90 is the neutral position) 
int servoPin=9; // analog 9 pin for servo
int servoDelay = 5000;  // Delay servo by 5 seconds 

Servo myTestSubject;  // Declare servo object

void setup() {
Serial.begin(9600);
myTestSubject.attach(servoPin);
}

void loop() {
pos=90;  //  Move servo to position 90 = the neutral position
myTestSubject.write(pos);
Serial.println(pos);  // Display position 
delay(servoDelay);
}