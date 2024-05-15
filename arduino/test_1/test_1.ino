int LED_pin_red_1 = 2;
int LED_pin_yellow_1 = 12;
int LED_pin_green_1 = 13;
int LED_pin_red_2 = 3;
int LED_pin_yellow_2 = 4;
int LED_pin_green_2 = 5;
int LED_pin_red_3 = 6;
int LED_pin_yellow_3 = 7;
int LED_pin_green_3 = 8;
int LED_pin_red_4 = 9;
int LED_pin_yellow_4 = 10;
int LED_pin_green_4 = 11;


void setup() {
  Serial.begin(9600);
  Serial.println("Setup Complete");
  pinMode(LED_pin_red_1, OUTPUT);
  pinMode(LED_pin_yellow_1, OUTPUT);
  pinMode(LED_pin_green_1, OUTPUT);
  pinMode(LED_pin_red_2, OUTPUT);
  pinMode(LED_pin_yellow_2, OUTPUT);
  pinMode(LED_pin_green_2, OUTPUT);
  pinMode(LED_pin_red_3, OUTPUT);
  pinMode(LED_pin_yellow_3, OUTPUT);
  pinMode(LED_pin_green_3, OUTPUT);
  pinMode(LED_pin_red_4, OUTPUT);
  pinMode(LED_pin_yellow_4, OUTPUT);
  pinMode(LED_pin_green_4, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char ch = Serial.read();
    Serial.print(ch);
    if (ch == 'a') {
      all_red();
    } else if (ch == 'b') {
      signal_1();
    } else if (ch == 'c') {
      signal_2();
    } else if (ch == 'd') {
      signal_3();
    } else if (ch == 'e') {
      signal_4();
    }
  } else {
  }
}


void all_red() {
  Serial.print("All Red");
  digitalWrite(LED_pin_red_1, HIGH);
  digitalWrite(LED_pin_red_2, HIGH);
  digitalWrite(LED_pin_red_3, HIGH);
  digitalWrite(LED_pin_red_4, HIGH);
  digitalWrite(LED_pin_yellow_2, LOW);
  digitalWrite(LED_pin_yellow_3, LOW);
  digitalWrite(LED_pin_yellow_4, LOW);
  digitalWrite(LED_pin_green_1, LOW);
  digitalWrite(LED_pin_green_2, LOW);
  digitalWrite(LED_pin_green_3, LOW);
  digitalWrite(LED_pin_green_4, LOW);
}

void signal_1() {
  Serial.print("Signal one");
  digitalWrite(LED_pin_red_1, HIGH);
  delay(1000);
  digitalWrite(LED_pin_red_1, LOW);
  digitalWrite(LED_pin_yellow_1, HIGH);
  delay(1000);
  digitalWrite(LED_pin_yellow_1, LOW);
  digitalWrite(LED_pin_green_1, HIGH);
}

void signal_2() {
  Serial.print("Signal three");
  digitalWrite(LED_pin_red_2, HIGH);
  delay(1000);
  digitalWrite(LED_pin_red_2, LOW);
  digitalWrite(LED_pin_yellow_2, HIGH);
  delay(1000);
  digitalWrite(LED_pin_yellow_2, LOW);
  digitalWrite(LED_pin_green_2, HIGH);
}

void signal_3() {
  Serial.print("Signal three");
  digitalWrite(LED_pin_red_3, HIGH);
  delay(1000);
  digitalWrite(LED_pin_red_3, LOW);
  digitalWrite(LED_pin_yellow_3, HIGH);
  delay(1000);
  digitalWrite(LED_pin_yellow_3, LOW);
  digitalWrite(LED_pin_green_3, HIGH);
}

void signal_4() {
  Serial.print("Signal three");
  digitalWrite(LED_pin_red_4, HIGH);
  delay(1000);
  digitalWrite(LED_pin_red_4, LOW);
  digitalWrite(LED_pin_yellow_4, HIGH);
  delay(1000);
  digitalWrite(LED_pin_yellow_4, LOW);
  digitalWrite(LED_pin_green_4, HIGH);
}
