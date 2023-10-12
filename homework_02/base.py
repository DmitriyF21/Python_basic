from homework_02.exceptions import LowFuelError, NotEnoughFuel
class Vehicle:
    pass

    def __init__(self, weight=None, started=False, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = started
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


car = Vehicle('1500', started=False, fuel=50, fuel_consumption=10)
car.start()
car.move(100)
print(car.started)