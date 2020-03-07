#include "moisture.h"
#include "light.h"
#include "DHT.h"

Moisture moisture;
Light light;
DHT dht(4, DHT11);

void setup() {
  // put your setup code here, to run once:
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
  // put your main code here, to run repeatedly:
  Serial.print(moisture.readMoisturePercentage());
  Serial.print(", ");
  Serial.print(light.readLightPercentage());
  Serial.print(", ");
  Serial.print(dht.readHumidity());
  Serial.print(", ");
  Serial.println(dht.readTemperature());
  delay(100);
}
