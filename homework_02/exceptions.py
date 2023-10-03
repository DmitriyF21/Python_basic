"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
2
class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass

class CargoOverload(Exception):
    pass