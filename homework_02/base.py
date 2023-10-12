from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC
class Vehicle:
    pass
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        try:
            if not self.started:
                if self.fuel > 0:
                    self.started = True
                else:
                    raise LowFuelError
        except LowFuelError:
            print('Топлива нет')

    def move(self, distance):
        try:
            if self.started:
                fuel_need = distance * self.fuel_consumption
                if self.fuel > fuel_need:
                    self.fuel -= fuel_need
                else:
                    raise NotEnoughFuel
        except NotEnoughFuel:
            print('Нет топлива')


car1 = Vehicle(1500, 50, 10)
print(car1)