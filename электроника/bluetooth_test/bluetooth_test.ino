int cnt = 0;    // счетчик

void setup() {
   Serial1.begin(9600);   // инициализация порта
}
  
void loop() {
   cnt++;
   Serial1.print("Hello BB from Arduino! Counter:");  // выводим надпись
   Serial1.println(cnt);    // выводим значение счетчика и переводим на новую строку
   delay(1000);   // ждем 1 секунду
}
