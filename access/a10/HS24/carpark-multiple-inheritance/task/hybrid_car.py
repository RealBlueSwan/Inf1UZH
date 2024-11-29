#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if not all(isinstance(param, (int, float)) and param > 0 for param in [gas_capacity, gas_per_100km, battery_size, battery_range_km]):
            raise Warning("Invalid initialization parameters")
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        # Starts with electro
        self.mode = 0       # 0 for electro, 1 for gas?

    def switch_to_combustion(self):
        if self.get_remaining_range() == 0:
            raise Warning
        self.mode = 1

    def switch_to_electric(self):
        if self.get_remaining_range() == 0:
            raise Warning
        self.mode = 0

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)


    def drive(self, dist):
        if not isinstance(dist, (int, float)) or dist < 0:
            raise Warning("Invalid distance")
        if self.mode == 0:
            if ElectricCar.get_remaining_range(self) >= dist:
                ElectricCar.drive(self, dist)
            else:
                remaining_electric_range = ElectricCar.get_remaining_range(self)
                ElectricCar.drive(self, remaining_electric_range)
                dist -= remaining_electric_range
                self.switch_to_combustion()
                CombustionCar.drive(self, dist)
        elif self.mode == 1:
            if CombustionCar.get_remaining_range(self) >= dist:
                CombustionCar.drive(self, dist)
            else:
                remaining_combustion_range = CombustionCar.get_remaining_range(self)
                CombustionCar.drive(self, remaining_combustion_range)
                dist -= remaining_combustion_range
                self.switch_to_electric()
                ElectricCar.drive(self, dist)


