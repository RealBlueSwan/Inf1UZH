#!/usr/bin/env python3

from unittest import TestCase
from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


class TestCars(TestCase):

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_electric_remaining_range(self):
        e = ElectricCar(25.0, 500.0)
        self.assertAlmostEqual(500.0, e.get_remaining_range(), delta=0.001)

    def test_electric_drive(self):
        e = ElectricCar(25.0, 500.0)
        e.drive(100.0)
        self.assertAlmostEqual(20.0, e.get_battery_status()[0], delta=0.001)

    def test_hybrid_switch_modes(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        self.assertEqual(h.mode, 1)
        h.switch_to_electric()
        self.assertEqual(h.mode, 0)


    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
