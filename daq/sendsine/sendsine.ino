void setup() {
  Serial.begin(1000000);
}

void loop() {
  Serial.print(micros());
  Serial.print('\n');
}
