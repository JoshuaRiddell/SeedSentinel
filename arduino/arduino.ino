#include "moisture.h"
#include "light.h"
#include "DHT.h"
#include <ArduinoJson.h>
#include <RF24.h>

Moisture moisture;
Light light;
DHT dht(4, DHT11);
RF24 radio(9, 8);

const byte address[6] = "pi001";
//const uint64_t address = 0x7069303031;

void setup() {
  pinMode(7, OUTPUT);
  digitalWrite(7, LOW);
  
  Serial.begin(115200);

  moisture.setPowerPin(2);
  moisture.setReadPin(A0);
  moisture.setup();

  light.setPowerPin(3);
  light.setReadPin(A1);
  light.setup();

  dht.begin();

  radio.begin();
  radio.openWritingPipe(address);
  radio.stopListening();
}

void loop() {
  //waitForSerialAvailable();
  //if (getDataCommandReceived()) {
    sendJsonData();
    delay(1000);
  //}
}

void waitForSerialAvailable() {
  while (!Serial.available());
}

bool getDataCommandReceived() {
  return Serial.read() == '?';
}

void sendJsonData() {
  StaticJsonDocument<1024> doc;
  buildJson(doc);
  sendJsonAsString(doc);
}

void buildJson(StaticJsonDocument<1024> &doc) {
  doc["moisture"] = moisture.readMoisturePercentage();
  doc["light"] = light.readLightPercentage();
  doc["humidity"] = dht.readHumidity();
  doc["temperature"] = dht.readTemperature();
}

void sendJsonAsString(StaticJsonDocument<1024> &doc) {
  String output;
  serializeJson(doc, output);
  Serial.println(output);

  char text[] = "Hello world";
  radio.write(text, sizeof(text));
}
