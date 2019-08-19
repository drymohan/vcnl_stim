uint8_t in_data;
const int outputPins[] = {2,3,4,5,6,7, 8, 9};
uint8_t outputData[8] = {0};
int i;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  Serial.println("Arduino Connected");

  for(auto pin: outputPins) pinMode(pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

//  for(int i=0; i<8; i++) {
//    digitalWrite(outputPins[i], HIGH);
//  }
//  digitalWrite(3, HIGH);
//  delay(500);
//  for(int i=0; i<8; i++) {
//    digitalWrite(outputPins[i], LOW);
//  }
//  digitalWrite(3, LOW);
//  delay(500);


  if (Serial.available() > 0) {
    in_data = Serial.read();


    for(int i=0; i<8; i++) {
//      Serial.println(bitRead(in_data, i));
      digitalWrite(outputPins[i], bitRead(in_data, i));
    }

  }

}
