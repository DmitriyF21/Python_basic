"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
class Plane(Vehicle):
    pass
    def __init__(self, cargo, max_cargo, weight=None, started=None, fuel=None, fuel_consumption=None):
        Vehicle().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        super().__init__(self.max_cargo)

    def load_cargo(self, value):
        pass

    def remove_all_cargo(self):
        pass