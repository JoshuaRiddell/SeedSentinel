#include "analog_power.h"

class Moisture : public AnalogPower {
public:
  double readMoisturePercentage() {
    return readAnalogPercentage();
  }
};
