"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
class Plane(Vehicle):
    pass
    def __init__(self, cargo, max_cargo, weight=None,  fuel=None, fuel_consumption=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, spec_num):
        expected = spec_num + self.cargo
        if self.max_cargo > expected:
            self.cargo = expected
        else:
            raise CargoOverload('Перегруз')




    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo