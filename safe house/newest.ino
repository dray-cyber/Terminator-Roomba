
const int stepx = 3; 
const int dirx = 8;
const int stepy = 5; 
const int diry = 12;
int old_something;
int data;
void setup()
{
pinMode(stepx,OUTPUT); 
pinMode(dirx,OUTPUT);
pinMode(stepy,OUTPUT); 
pinMode(diry,OUTPUT);
Serial.begin(9600);
}
void loop() {
int start = 180;
int data = Serial.parseInt();
int something = data;
if (something != old_something){
Serial.println(something);  // display if it changed
old_something = something;
digitalWrite(diry, LOW); // anticlockwise
if (data>1) {
  for(int x = 0; x < data; x++) {
    digitalWrite(stepy,HIGH);
    delayMicroseconds(500);
    digitalWrite(stepy,LOW);
    delayMicroseconds(500);
  }}} 
  }
  
