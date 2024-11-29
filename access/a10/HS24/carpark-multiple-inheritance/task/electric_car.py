#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not isinstance(battery_size, (int, float)) or battery_size <= 0:
            raise Warning("Invalid battery size")
        if not isinstance(battery_range_km, (int, float)) or battery_range_km <= 0:
            raise Warning("Invalid battery range")
        #ElectricCars are initiated with a battery_size in kilo-watt hours and the range of a fully charged battery in kilometers.
        self.battery_size = battery_size
        self.current_battery = battery_size
        self.battery_range_km = battery_range_km

    def charge(self, kwh):
        if self.current_battery + kwh > self.battery_size:
            raise Warning("Overcharge")
        self.current_battery += kwh

    def get_battery_status(self):
        return self.current_battery, self.battery_size

    def get_remaining_range(self):
        return self.current_battery / self.battery_size * self.battery_range_km

    def drive(self, dist):
        if not isinstance(dist, (int, float)) or dist < 0:
            raise Warning("Invalid distance")
        required_battery = self.battery_size / self.battery_range_km * dist
        if self.current_battery < required_battery:
            self.current_battery = 0
            raise Warning("Tank depleted")
        self.current_battery -= required_battery
