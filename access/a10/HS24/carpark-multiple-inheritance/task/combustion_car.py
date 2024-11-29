#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not isinstance(gas_capacity, (int, float)) or gas_capacity <= 0:
            raise Warning("Invalid gas capacity")
        if not isinstance(gas_per_100km, (int, float)) or gas_per_100km <= 0:
            raise Warning("Invalid gas consumption rate")
        self.gas_capacity = gas_capacity
        self.gas_per_100km = gas_per_100km
        self.current_gas = gas_capacity

    def fuel(self, f):
        if self.current_gas + f > self.gas_capacity:
            self.current_gas = 0
            raise Warning("Overfilled")
        self.current_gas += f

    def get_gas_tank_status(self):
        return self.current_gas, self.gas_capacity

    def get_remaining_range(self):
        return self.current_gas / self.gas_per_100km * 100

    def drive(self, dist):
        if not isinstance(dist, (int, float)) or dist < 0:
            raise Warning("Invalid distance")
        required_gas = self.gas_per_100km / 100 * dist
        if self.current_gas < required_gas:
            self.current_gas = 0
            raise Warning("Tank depleted")
        self.current_gas -= required_gas
