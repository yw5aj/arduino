#define FASTADC 1  // Flag for prescale 16
// Code pasted for modifying ADCSRA
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup() {
  Serial.begin(1000000);
  #if FASTADC
    // set prescale to 16
    sbi(ADCSRA,ADPS2) ;
    cbi(ADCSRA,ADPS1) ;
    cbi(ADCSRA,ADPS0) ;
  #endif
}

void loop() {
  int val;
  val = analogRead(A0) / 4;  // Convert to 8-bit
  Serial.write(val);
}
