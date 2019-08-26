uint8_t in_data;
const int outputPins[] = {2,3,4,5,6,7, 8, 9};
//uint8_t outputData[8] = {0};
int i;
// For extracting bits
uint8_t one_bit;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  Serial.println("Arduino Connected");

  for(auto pin: outputPins) pinMode(pin, OUTPUT);

//  For CED flag
  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);
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

//    Serial.println(in_data);

//  If 0, then send flag
    if (in_data == 0) {
      digitalWrite(12, LOW);
      digitalWrite(12, HIGH);
      }

    else {
      for(int i=0; i<8; i++) {
//        Serial.println(bitRead(in_data, i));
        digitalWrite(outputPins[i], bitRead(in_data, i));
//        Experimental ... may be quicker way of extracting relevant bit
//        digitalWrite(outputPins[i], (in_data>>i)&one_bit);
      }
    }

  }

}
