"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    pass

    def __init__(self, weight=None,  fuel=None, fuel_consumption=None, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, spec_num):
        if self.max_cargo > 0:
            expected = spec_num + self.cargo
            if self.max_cargo >= expected:
                self.cargo = expected
            else:
                raise CargoOverload

    def remove_all_cargo(self):
        if self.cargo > 0:
            prev_cargo = self.cargo
            self.cargo = 0
            return prev_cargo


# air = Plane(30,250,3000,1500,15)
# air.load_cargo(40)
# air.remove_all_cargo()