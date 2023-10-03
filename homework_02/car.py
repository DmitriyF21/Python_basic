"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Venicle

class Car(Venicle):
    pass
    def __init__(self, engine, weight=None, started=None, fuel=None, fuel_consumption=None):
        Venicle().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self):
        pass