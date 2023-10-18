"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    pass

    def __init__(self, weight=None, fuel=None, fuel_consumption=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
        return self.engine
#
# car = Car(1,2,3,4)
# engin = Engine(2000,4)
# car.set_engine(engine)
# print(car.engine)


eng = Engine(volume= 2000,pistons= 4)
car = Car( weight=2000,  fuel=150, fuel_consumption=15)
car.set_engine(eng)
print(car.engine)