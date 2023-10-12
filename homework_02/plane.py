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
        self.started = False
        self.max_cargo = max_cargo

    def load_cargo(self, spec_num):
        try:
            if self.cargo == 0:
                if self.max_cargo > 0:
                    expected = spec_num + self.cargo
                    if expected < self.max_cargo:
                        self.cargo += expected
                    else:
                        raise CargoOverload
        except CargoOverload:
            print('Перегруз')



    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo
