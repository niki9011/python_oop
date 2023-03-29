import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(25.5, 210.5)

    def test_initialization(self):
        self.assertEqual(self.vehicle.fuel, 25.5)
        self.assertEqual(self.vehicle.horse_power, 210.5)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_driver_not_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_valid(self):
        self.vehicle.drive(2)
        self.assertEqual(23, self.vehicle.fuel)

    def test_refuel_not_more_space(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_valid(self):
        self.vehicle.fuel = 18
        self.vehicle.refuel(2)
        self.assertEqual(self.vehicle.fuel, 20)

    def test__str__(self):
        self.assertEqual("The vehicle has 210.5 " +
                         "horse power with 25.5 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    unittest.main()
