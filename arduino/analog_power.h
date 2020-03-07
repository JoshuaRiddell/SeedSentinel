#ifndef ANALOG_POWER_H
#define ANALOG_POWER_H

class AnalogPower {
public:
  void setPowerPin(int pin) {
    powerPin = pin;
  }

  void setReadPin(int pin) {
    readPin = pin;
  }

  void setup() {
    setupPowerOutput();
    powerOff();
  }

  double readAnalogPercentage() {
    double analogPercentage;

    powerOn();
    analogPercentage = readAnalogPinAsPercentage();
    powerOff();

    return analogPercentage;
  }

private:
  void setupPowerOutput() {
    pinMode(powerPin, OUTPUT);
  }

  void powerOn() {
    digitalWrite(powerPin, HIGH);
    delay(1000);
  }

  void powerOff() {
    digitalWrite(powerPin, LOW);
  }

  double readAnalogPinAsPercentage() {
    return analogRead(readPin) / 1023.;
  }

  int powerPin;
  int readPin;
};

#endif
