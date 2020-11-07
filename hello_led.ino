void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(11250);
}

void loop() {
  // Hel-
  Serial.print("Hel");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
  delay(100);
  // -lo
  Serial.print("lo, ");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
  
  delay(600);

  // World
  Serial.print("World!");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
  
  delay(1000); // 2 seconds a loop
  Serial.print("\r\n");
}
