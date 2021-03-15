
const int stepx = 3; 
const int dirx = 8;
const int stepy = 5; 
const int diry = 12;
void setup()
{
pinMode(stepy,OUTPUT); 
pinMode(diry,OUTPUT);
Serial.begin(9600);
digitalWrite(diry, LOW); // anticlockwise
}
void loop() {
int data = Serial.parseInt();
if (data == 400){
digitalWrite(diry, LOW); // anticlockwise
}
if (data == 401){
digitalWrite(diry, HIGH); // anticlockwise
}
if (data>1 and data < 300) {
  for(int x = 0; x < data; x++) {
    digitalWrite(stepy,HIGH);
    delayMicroseconds(500);
    digitalWrite(stepy,LOW);
    delayMicroseconds(500);
  }}
  } 
  
  
