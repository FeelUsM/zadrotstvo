/* SFE_BMP180 altitude example sketch

This sketch shows how to use the Bosch BMP180 pressure sensor
as an altimiter.
https://www.sparkfun.com/products/11824

Like most pressure sensors, the BMP180 measures absolute pressure.
Since absolute pressure varies with altitude, you can use the pressure
to determine your altitude.

Because pressure also varies with weather, you must first take a pressure
reading at a known baseline altitude. Then you can measure variations
from that pressure

Hardware connections:

- (GND) to GND
+ (VDD) to 3.3V

(WARNING: do not connect + to 5V or the sensor will be damaged!)

You will also need to connect the I2C pins (SCL and SDA) to your
Arduino. The pins are different on different Arduinos:

Any Arduino pins labeled:  SDA  SCL
Uno, Redboard, Pro:        A4   A5
Mega2560, Due:             20   21
Leonardo:                   2    3

Leave the IO (VDDIO) pin unconnected. This pin is for connecting
the BMP180 to systems with lower logic levels such as 1.8V

Have fun! -Your friends at SparkFun.

The SFE_BMP180 library uses floating-point equations developed by the
Weather Station Data Logger project: http://wmrx00.sourceforge.net/

Our example code uses the "beerware" license. You can do anything
you like with this code. No really, anything. If you find it useful,
buy me a beer someday.

V10 Mike Grusin, SparkFun Electronics 10/24/2013
V1.1.2 Updates for Arduino 1.6.4 5/2015
*/

// Your sketch must #include this library, and the Wire library.
// (Wire is a standard library included with Arduino.):

#include <SFE_BMP180.h>
#include <Wire.h>

// You will need to create an SFE_BMP180 object, here called "pressure":

SFE_BMP180 pressure;

double baseline; // baseline pressure

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial.println("REBOOT");

  // Initialize the sensor (it is important to get calibration values stored on the device).

  if (pressure.begin())
    Serial.println("BMP180 init success");
  else
  {
    // Oops, something went wrong, this is usually a connection problem,
    // see the comments at the top of this sketch for the proper connections.

    Serial.println("BMP180 init fail (disconnected?)\n\n");
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
    +String(Pressure*100,0)
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
    Serial1.print("$");       
    Serial1.print(str_out);
    Serial1.print("*");
    Serial1.println(checksum_end, HEX);
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
  char status;
  double T,P,p0,a;

  // You must first get a temperature measurement to perform a pressure reading.
  
  // Start a temperature measurement:
  // If request is successful, the number of ms to wait is returned.
  // If request is unsuccessful, 0 is returned.

  status = pressure.startTemperature();
  if (status != 0)
  {
    // Wait for the measurement to complete:

    delay(status);

    // Retrieve the completed temperature measurement:
    // Note that the measurement is stored in the variable T.
    // Use '&T' to provide the address of T to the function.
    // Function returns 1 if successful, 0 if failure.

    status = pressure.getTemperature(T);
    if (status != 0)
    {
      // Start a pressure measurement:
      // The parameter is the oversampling setting, from 0 to 3 (highest res, longest wait).
      // If request is successful, the number of ms to wait is returned.
      // If request is unsuccessful, 0 is returned.

      status = pressure.startPressure(3);
      if (status != 0)
      {
        // Wait for the measurement to complete:
        delay(status);

        // Retrieve the completed pressure measurement:
        // Note that the measurement is stored in the variable P.
        // Use '&P' to provide the address of P.
        // Note also that the function requires the previous temperature measurement (T).
        // (If temperature is stable, you can do one temperature measurement for a number of pressure measurements.)
        // Function returns 1 if successful, 0 if failure.

        status = pressure.getPressure(P,T);
        if (status != 0)
        {
          return(P);
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
  else Serial.println("error starting temperature measurement\n");
  return 0.;
}
