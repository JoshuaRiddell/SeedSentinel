#include "analog_power.h"

class Light : public AnalogPower {
public:
  double readLightPercentage() {
    return 1.-readAnalogPercentage();
  }
};
