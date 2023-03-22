from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def consumption_fuel(self, distance, ac_consumption):
        consumption_drive = (self.fuel_consumption + ac_consumption) * distance
        if self.fuel_quantity >= consumption_drive:
            self.fuel_quantity -= consumption_drive


class Car(Vehicle):

    def drive(self, distance):
        ac_consumption = 0.9
        Vehicle.consumption_fuel(self, distance, ac_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance):
        ac_consumption = 1.6
        Vehicle.consumption_fuel(self, distance, ac_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
