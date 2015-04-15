#define FASTADC 1
// defines for setting and clearing register bits
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

int value[100];   // variable to store the value coming from the sensor
int i=0;

void setup() 
{
 Serial.begin(9600) ;
 int i ;
  
#if FASTADC
  // set prescale to 16
  sbi(ADCSRA,ADPS2) ;
  cbi(ADCSRA,ADPS1) ;
  cbi(ADCSRA,ADPS0) ;
#endif
}

void loop() 
{ 
 for (i=0;i<100;i++)
{
  value[i]=analogRead(0);
} 
for (i=0;i<100;i++)
{
    Serial.println(value[i]);
    Serial.println(micros());
} 
Serial.println();
Serial.println();
Serial.println();
delay(5000);
  
}
