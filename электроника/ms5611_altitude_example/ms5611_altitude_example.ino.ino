/*
  MS5611 Barometric Pressure & Temperature Sensor. Output for MS5611_processing.pde
  Read more: http://www.jarzebski.pl/arduino/czujniki-i-sensory/czujnik-cisnienia-i-temperatury-ms5611.html
  GIT: https://github.com/jarzebski/Arduino-MS5611
  Web: http://www.jarzebski.pl
  (c) 2014 by Korneliusz Jarzebski
 */

// Your sketch must #include this library, and the Wire library.
// (Wire is a standard library included with Arduino.):

#include <MS5611.h>
#include <Wire.h>

// You will need to create an SFE_BMP180 object, here called "pressure":

MS5611 pressure;
// SFE_BMP180 pressure;
#define LED_BUILTIN 13
double baseline; // baseline pressure

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  //Serial1.begin(9600);
  Serial.println("REBOOT");

  // Initialize the sensor (it is important to get calibration values stored on the device).

  if (pressure.begin(MS5611_ULTRA_HIGH_RES))
    Serial.println("MS5611 init success");
  else
  {
    // Oops, something went wrong, this is usually a connection problem,
    // see the comments at the top of this sketch for the proper connections.

    Serial.println("MS5611 init fail (disconnected?)\n\n");
    while(1){ // Pause forever.
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(1000);                       // wait for a second
     
    }
  }

  // Get the baseline pressure:
  /*
  baseline = 1013.25;
  
  Serial.print("baseline pressure: ");
  Serial.print(baseline);
  Serial.println(" mb");  
  */
}


uint32_t get_time = millis();
double sum = 0;
uint8_t n = 0;

void loop()
{
  double a,Pressure;
  Pressure = getPressure();

  sum += Pressure;
  n += 1;
  if (millis() >= (get_time + (100))) //every 100 milli-seconds send NMEA output over serial port
  {
    get_time = millis();
    Pressure = sum / n ;
    sum=0; n=0;
    // Get a new pressure reading:
  
    // Show the relative altitude difference between
    // the new reading and the baseline reading:
  
    //a = pressure.altitude(P,baseline);
  
    /*
    Serial.print("P= ");
    Serial.print(P,2);
    Serial.print(" mb, absolute altitude: ");
    if (a >= 0.0) Serial.print(" "); // add a space for positive numbers
    Serial.print(a,1);
    Serial.print(" meters, ");
    if (a >= 0.0) Serial.print(" "); // add a space for positive numbers
    Serial.print(a*3.28084,0);
    Serial.println(" feet");
  */
    //$LK8EX1,pressure,altitude,vario,temperature,battery,*checksum
    //$LK8EX1,pressure,99999,9999,temp,999,*checksum
    String str_out = String("LK8EX1,")
    +String(Pressure,0)
    +String(",0,9999,")
    +String("99")
    +String(",999,");
  
    unsigned int checksum_end, ai, bi;        // Calculating checksum for data string
    for (checksum_end = 0, ai = 0; ai < str_out.length(); ai++)
    {
      bi = (unsigned char)str_out[ai];
      checksum_end ^= bi;
    }
    Serial.print("$");       
    Serial.print(str_out);
    Serial.print("*");
    Serial.println(checksum_end, HEX);
   // Serial1.print("$");       
   // Serial1.print(str_out);
   // Serial1.print("*");
   // Serial1.println(checksum_end, HEX);
  /*  Serial.print("$LK8EX1,");
    Serial.print(P*100,0);
    Serial.println(",99999,9999,99,999");
    Serial1.print("$LK8EX1,");
    Serial1.print(P*100,0);
    Serial1.println(",99999,9999,99,999");*/
    /*
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(50);                       // wait for a second*/
  }
}


double getPressure()
{
  long realPressure = pressure.readPressure();
  double tmp;
  tmp = realPressure;
  return tmp;
}
