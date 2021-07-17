#define Print(x) ({Serial.print(#x " = ");\
                   Serial.println(x);})

void setup() {
  Serial.begin(9600);
}


void sizes(){
  Print(sizeof(long int));  
  Print(sizeof(int));    
  Print(sizeof(short));
  Print(sizeof(word));  
  Print(sizeof(byte));  
  Print(sizeof(size_t));  
}


void loop() {
  String x;
  while (Serial.available()) {
    x = Serial.readStringUntil('\n');
    switch (x[0]) {
      case 'y':
      case 'Y': sizes(); break;
      default: break;
    }
  }
}
