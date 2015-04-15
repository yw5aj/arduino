#define FASTADC 1  // Flag for prescale 16
// Code pasted for modifying ADCSRA
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup() {
  // I tested it and it seems 200,000 is the highest w/o too many failures
  Serial.begin(200000);
  #if FASTADC
    // set prescale to 16
    sbi(ADCSRA,ADPS2) ;
    cbi(ADCSRA,ADPS1) ;
    cbi(ADCSRA,ADPS0) ;
  #endif
}

void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
}
