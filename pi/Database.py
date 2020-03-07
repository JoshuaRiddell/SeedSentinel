#!/usr/bin/env python3

from influxdb import InfluxDBClient
import json

class DatabaseInterface(object):
    def __init__(self, url):
        # get rpi password from file
        pi_password = ""
        with open("password.txt", "r") as pw_fd:
            pi_password = pw_fd.read().strip()

        # connect to the database
        self.client = InfluxDBClient(url, 8086, 'pi', pi_password, database='garden')

        # save the request template in ram for easy access
        self.request_template = {}
        with open("request_template.json", 'r') as f:
            self.request_template = dict(json.load(f))

    def log_soil(self, moisture, plant_type="", plant_id=0): # and temperature in future
        fields = {
            "moisture": moisture,
        }
        self.log_measurement("soil", fields, plant_type, plant_id)
    
    def log_atmosphere(self, temperature, humidity, plant_type="", plant_id=0): # and pressure in future
        fields = {
            "temperature": temperature,
            "humidity": humidity,
        }
        self.log_measurement("atmosphere", fields, plant_type, plant_id)
    
    def log_environmental(self, light, plant_type="", plant_id=0):
        fields = {
            "light": light,
        }
        self.log_measurement("environmental", fields, plant_type, plant_id)

    def log_measurement(self, measurement, fields, plant_type, plant_id):
        tmp = self.request_template.copy()

        tmp["measurement"] = measurement
        tmp["fields"] = fields
        tmp["tags"]["plant-type"] = plant_type
        tmp["tags"]["plant-id"] = plant_id

        self.client.write_points([tmp])
