class Car:
    def __init__(self, engine) -> None:
        self.engine = engine


class GasEngine:
    def __init__(self, horse_power) -> None:
        self.hp = horse_power

    def start(self):
        print("Starting {}hp gas engine".format(self.hp))


class DieselEngine:
    def __init__(self, horse_power) -> None:
        self.hp = horse_power

    def start(self):
        print("Starting {}hp diesel engine".format(self.hp))


my_car_gas = Car(GasEngine(4))
my_car_gas.engine.start()

my_car_diesel = Car(DieselEngine(2))
my_car_diesel.engine.start()
