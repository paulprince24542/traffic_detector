int LED_pin_red = 2;
int LED_pin_yellow = 3;
int LED_pin_green = 4;

int LED_pin_red_1 = 8;
int LED_pin_yellow_2 = 9;
int LED_pin_green_3 = 10;

void setup() {
  Serial.begin(115200);
  Serial.println("Setup Complete");
  pinMode(LED_pin_red, OUTPUT);
  pinMode(LED_pin_yellow, OUTPUT);
  pinMode(LED_pin_green, OUTPUT);
  pinMode(LED_pin_red_1, OUTPUT);
  pinMode(LED_pin_yellow_2, OUTPUT);
  pinMode(LED_pin_green_3, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char ch = Serial.read();
    if (ch == 'a') {
      initial_state();
    } else if (ch == 'b') {
      first_Signal_Go();
    } else if (ch == 'c') {
      second_Signal_Go();
    } else if (ch == 'd') {
      red_light();
    } else {
    }
  } else {
  }
}


void red_light() {
  Serial.print("All Red");
  digitalWrite(LED_pin_red, HIGH);
  digitalWrite(LED_pin_red_1, HIGH);
  digitalWrite(LED_pin_yellow, LOW);
  digitalWrite(LED_pin_green, LOW);
  digitalWrite(LED_pin_yellow_2, LOW);
  digitalWrite(LED_pin_green_3, LOW);
}


void first_Signal_Go() {
  Serial.print("Signal One");
  digitalWrite(LED_pin_red_1, HIGH);
  digitalWrite(LED_pin_red, HIGH);
  digitalWrite(LED_pin_green_3, LOW);
  delay(1000);
  digitalWrite(LED_pin_red, LOW);
  digitalWrite(LED_pin_yellow, HIGH);
  delay(1000);
  digitalWrite(LED_pin_yellow, LOW);
  digitalWrite(LED_pin_green, HIGH);
}


void second_Signal_Go() {
  Serial.print("Signal Two");

  //Signal 1 State
  digitalWrite(LED_pin_red, HIGH);
  digitalWrite(LED_pin_yellow, LOW);
  digitalWrite(LED_pin_green, LOW);

   digitalWrite(LED_pin_red_1, LOW);
  digitalWrite(LED_pin_yellow_2, LOW);
  digitalWrite(LED_pin_green_3, LOW);

  // Signal 2 State
  digitalWrite(LED_pin_red_1, HIGH);
  delay(1000);
  digitalWrite(LED_pin_red_1, LOW);
  digitalWrite(LED_pin_yellow_2, HIGH);
  delay(1000);
  digitalWrite(LED_pin_yellow_2, LOW);
  digitalWrite(LED_pin_green_3, HIGH);
}

void initial_state() {
  digitalWrite(LED_pin_red, LOW);
  digitalWrite(LED_pin_red_1, LOW);
  digitalWrite(LED_pin_yellow, LOW);
  digitalWrite(LED_pin_yellow_2, LOW);
  digitalWrite(LED_pin_green, LOW);
  digitalWrite(LED_pin_green_3, LOW);
}
