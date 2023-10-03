"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
class Plane(Vehicle):
    pass
    def __init__(self,cargo, max_cargo, weight=None, started=None, fuel=None, fuel_consumption=None):
        Vehicle().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo


