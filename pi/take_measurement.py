#!/usr/bin/env python3

from Database import DatabaseInterface
from Arduino import Arduino

def main():
    db = DatabaseInterface("riddell.dev")
    arduino = Arduino()

    data = arduino.read_sensors_with_retry()

    db.log_atmosphere(data["temperature"],
                        data["humidity"])

    db.log_environmental(data["light"])

    db.log_soil(data["moisture"])

if __name__ == "__main__":
    main()