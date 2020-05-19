void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // He-
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
  delay(100);
  // -llo
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
  
  delay(600);

  // World
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
  
  delay(1000); // 2 seconds a loop
}
