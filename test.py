#!/usr/bin/env python3

from influxdb import InfluxDBClient
import json

measurements = {
    "soil": {
        "moisture": 0.0,
        "temperature": 0.0,
    },
    "atmosphere": {
        "temperature": 0.0,
        "humidity": 0.0,
        "pressure": 0.0,
    },
    "environmental": {
        "light": 0.0,
        "rainfall": 0.0,
    }
}

pi_password = ""
with open("password.txt", "r") as pw_fd:
    pi_password = pw_fd.read().strip()

client = InfluxDBClient('riddell.dev', 8086, 'pi', pi_password,
                        database='garden', ssl=True, verify_ssl=True)

request_template = {}
with open("request_template.json", 'r') as f:
    request_template = dict(json.load(f))

def log_measurement(measurement, fields, plant_type="", plant_id=0):
    tmp = request_template.copy()
    tmp["measurement"] = measurement
    tmp["fields"] = fields
    tmp["tags"]["plant-type"] = plant_type
    tmp["tags"]["plant-id"] = plant_id
    client.write_points([tmp])

log_measurement("soil", {
    "moisture": 0.5,
    "temperature": 25.1,
}, plant_type="blueberry", plant_id=1)

log_measurement("air", {
    "temperature": 0.5,
    "humidity": 0.0,
}, plant_type="blueberry", plant_id=1)

log_measurement("air", {
    "temperature": 0.5,
    "humidity": 0.0,
}, plant_type="blueberry", plant_id=1)
