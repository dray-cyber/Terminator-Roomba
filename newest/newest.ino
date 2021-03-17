
const int stepy = 3; 
const int diry = 8;
const int stepx = 5; 
const int dirx = 12;
void setup()
{
pinMode(stepy,OUTPUT); 
pinMode(diry,OUTPUT);
pinMode(stepx,OUTPUT); 
pinMode(dirx,OUTPUT);
Serial.begin(9600);
digitalWrite(diry, LOW); // anticlockwise
}
void loop() {
int data = Serial.parseInt();
if (data == 400){
digitalWrite(dirx, LOW); // anticlockwise
}
if (data == 401){
digitalWrite(dirx, HIGH); // anticlockwise
}
if (data == 500){
digitalWrite(diry, LOW); // anticlockwise
}
if (data == 501){
digitalWrite(diry, HIGH); // anticlockwise
}
if (data < 300) {
  for(int x = 0; x < data; x++) {
    digitalWrite(stepx,HIGH);
    delayMicroseconds(500);
    digitalWrite(stepx,LOW);
    delayMicroseconds(500);
  }}
if (data > 600) {
  int stepstogo = data - 600;
  for(int x = 0; x < stepstogo; x++) {
    digitalWrite(stepy,HIGH);
    delayMicroseconds(500);
    digitalWrite(stepy,LOW);
    delayMicroseconds(500);
  }}

  } 
  
  
