#include "moisture.h"
#include "light.h"
#include "DHT.h"
#include <ArduinoJson.h>

Moisture moisture;
Light light;
DHT dht(4, DHT11);

void setup() {
  Serial.begin(115200);

  moisture.setPowerPin(2);
  moisture.setReadPin(A0);
  moisture.setup();

  light.setPowerPin(3);
  light.setReadPin(A1);
  light.setup();

  dht.begin();
}

void loop() {
  waitForSerialAvailable();
  if (getDataCommandReceived()) {
    sendJsonData();
  }
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
}
