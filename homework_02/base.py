from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class Vehicle(ABC):
    pass

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if not self.started:
            if self.fuel >= 0:
                self.started = True
            else:
                raise LowFuelError
        else:
            if self.fuel == 0:
                raise LowFuelError
        if self.fuel_consumption > 0:
            if self.fuel < distance * self.fuel_consumption:
                raise NotEnoughFuel
            else:
                self.fuel -= distance * self.fuel_consumption


car1 = Vehicle(1500, 50, 10)
car1.start()
car1.move(3)
print(car1.fuel)