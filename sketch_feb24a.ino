
const int stepx = 3; 
const int dirx = 4;
const int stepy = 5; 
const int diry = 6;
void setup()
{ 
pinMode(stepx,OUTPUT); 
pinMode(dirx,OUTPUT);
pinMode(stepy,OUTPUT); 
pinMode(diry,OUTPUT);
Serial.begin(9600);

while (!Serial);

}

void loop() {

if (Serial.available())

{
int data = Serial.parseInt();
int state = state.toInt()
if (state == 1)
{
  digitalWrite(dirx, LOW); // anticlockwise
  digitalWrite(stepx,HIGH); 
  delayMicroseconds(500); 
  digitalWrite(stepx,LOW); 
  delayMicroseconds(500); 
//left
}
if (state == 2)
{
  digitalWrite(stepx,LOW); 
//stop
}
if (state == 3)
{
  digitalWrite(dirx, HIGH); // clockwise
  digitalWrite(stepx,HIGH); 
  delayMicroseconds(500); 
  digitalWrite(stepx,LOW); 
  delayMicroseconds(500);
  //right 
}
}
}
