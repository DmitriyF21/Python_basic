"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
class Car(Vehicle):
    pass
    def __init__(self, engine, weight=None, started=None, fuel=None, fuel_consumption=None):
        Vehicle().__init__(weight, started, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
        return self.engine

eng = Engine(volume= 2000,pistons= 4)
car = Car(engine=10, weight=2000, started=False, fuel=150, fuel_consumption=15)
car.set_engine(20)
print(car)