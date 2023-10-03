

class Vehicle:
    pass

    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, started, fuel):
        if not self.started:
            self.fuel > 0


