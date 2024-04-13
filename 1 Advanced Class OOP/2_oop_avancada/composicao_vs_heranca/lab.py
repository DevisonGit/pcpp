class Tyre:
    def __init__(self, size, pressure):
        self.size = size
        self.pressure = pressure

    def get_pressure(self):
        print(f"Tire Size {self.size} -> Pressure {self.pressure} psi")

    @staticmethod
    def pump():
        print("pump")


class Engine:
    def __init__(self, fuel_tipe):
        self.fuel_tipe = fuel_tipe
        self.state = "off"

    def start(self):
        print(f"Start the engine {self.fuel_tipe}")
        self.state = 'on'

    def stop(self):
        print(f"Stop the engine {self.fuel_tipe}")
        self.state = 'off'

    def get_status(self):
        print(f"Engine {self.fuel_tipe} Status {self.state}")


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


my_vehicle = Vehicle("Honda", engine=Engine('electric'), tires=Tyre(15, 32))
my_vehicle.engine.get_status()
my_vehicle.engine.start()
my_vehicle.engine.get_status()
my_vehicle.tires.get_pressure()
my_vehicle.engine.stop()
my_vehicle.engine.get_status()
print("*" * 30)
my_vehicle = Vehicle("Honda", engine=Engine('Gasoline'), tires=Tyre(18, 38))
my_vehicle.engine.get_status()
my_vehicle.engine.start()
my_vehicle.engine.get_status()
my_vehicle.tires.get_pressure()
my_vehicle.engine.stop()
my_vehicle.engine.get_status()
