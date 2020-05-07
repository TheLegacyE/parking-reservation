/*Parking Sensor Assistant*/
#define ledGreen 4
#define trigPin 7
#define echoPin 6
#define ledRed 8
#define buzzer 3

int sound = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
 
  pinMode(ledRed, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledGreen, OUTPUT);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.begin(9600); 
  long timeTaken, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  timeTaken = pulseIn(echoPin, HIGH);//determine distance of wave
  distance = (timeTaken/2)/29.1;//using timeTaken calc distance of object

  /*determine corressponding leds to light up with respect to the distance
  of object*/

  if((distance<100)&&(distance>5)){
      digitalWrite(ledGreen, HIGH);
      Serial.print(ledGreen);
      delay(300);
    }else{
      digitalWrite(ledGreen, LOW);
      }

    if((distance<5)&&(distance>0)){
      digitalWrite(ledRed, HIGH);
      Serial.print(ledRed);
      delay(300);
 
    }else{
     digitalWrite(ledRed,LOW);
     
      }

     
}
