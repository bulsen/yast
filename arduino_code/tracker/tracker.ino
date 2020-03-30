#include <Wire.h>
#include <LSM303.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// Network prefs
const char *ssid     = "TURKSAT-KABLONET-0AFA-2.4G";
const char *password = "05f5760c";

//server 
const char *server = "http://192.168.0.177";
const int port = 80;

// gyro init
LSM303 compass;

char report[80];

void setup()
{
  Serial.begin(9600);
  
  Wire.begin();
  compass.init();
  compass.enableDefault();
 
}

void loop()
{
  if(WiFi.status()== WL_CONNECTED){
  compass.read();
  
  snprintf(report, sizeof(report), "{\"x\":%6d,\"y\":%6d,\"z\":%6d}", compass.a.x, compass.a.y, compass.a.z);
  String Data = "{ \"data\" :  " + String(report)+ "}";
  
  HTTPClient http;
  //http.begin(address);
  http.begin("http://192.168.0.177/data_read");
  http.addHeader("Content-Type","application/json");
  int httpCode = http.POST(Data);
  String payload = http.getString(); 
  
  /*
  //debug
  Serial.println(payload);
  Serial.println(report);
  Serial.println(Data);
  Serial.println(address);
  Serial.println(httpCode);
  */
  http.end();
  }else{
 
    Serial.println("Error in WiFi connection");   
 
 }
  delay(1000);
}
