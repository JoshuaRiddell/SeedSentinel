import serial
import serial.tools.list_ports
import time
import json

class Arduino():
    def __init__(self):
        self.set_serial_port_by_scan()
        self._arduino_data = {}

    def set_serial_port(self, port):
        self._serial_port = port

    def set_serial_port_by_scan(self):
        comports_list = serial.tools.list_ports.comports()
        available_ports = [comport.device for comport in comports_list]
        self._serial_port = available_ports[0]

    def read_sensors_with_retry(self):
        for i in range(5):
            self._try_read_from_arduino()
            if self._data_is_valid():
                return self._arduino_data
            time.sleep(1)
            
        raise Exception("Could not read valid data from Arduino.")
    
    def read_sensors(self):
        self._try_read_from_arduino()
        if self._data_is_valid():
            return self._arduino_data
        
        raise Exception("Could not read valid data from Arduino.")

    def _try_read_from_arduino(self):
        try:
            self._read_from_arduino()
        except:
            self._teardown_serial_port()

    def _read_from_arduino(self):
        self._setup_serial_port()
        self._wait_for_arduino_boot()
        self._send_read_data_command()
        self._read_arduino_data()
        self._teardown_serial_port()

    def _data_is_valid(self):
        return self._arduino_data != {}

    def _setup_serial_port(self):
        self.serial_object = serial.Serial(self._serial_port)
        self.serial_object.timeout = 5
        self.serial_object.baudrate = 115200

    def _wait_for_arduino_boot(self):
        time.sleep(3)

    def _send_read_data_command(self):
        self.serial_object.write(b"?")

    def _read_arduino_data(self):
        serial_data = self.serial_object.readline()
        self._arduino_data = json.loads(serial_data)

    def _teardown_serial_port(self):
        self.serial_object.close()

if __name__ == "__main__":
    arduino = Arduino()
    print(arduino.read_sensors_with_retry())
