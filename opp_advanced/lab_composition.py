class Vehicle:
    def __init__(self, VIN, engine, tires) -> None:
        self.vin = VIN
        self.engine = engine
        self.tires = tires


class Tires:
    def __init__(self, size) -> None:
        self.size = size

    def get_pressure(self):
        print("Tire Pressure {}".format(self.size))

    def pump(self):
        print("Tire pump")


class Engine:
    def __init__(self, fuel_type) -> None:
        self.fuel_type = fuel_type
        self.state = False

    def start(self):
        print("Start a {} engine".format(self.fuel_type))
        self.state = True

    def stop(self):
        print("Stop a {} engine".format(self.fuel_type))
        self.state = False

    def get_state(self):
        print("Engine {} state {}".format(self.fuel_type, self.state))


city_tire = Tires(15)
off_road_tire = Tires(18)

eletric_engine = Engine("Eletric")
petrol_engine = Engine("Petrol")

car_city_engine = Vehicle("Honda", eletric_engine, city_tire)
car_city_engine.engine.start()
car_city_engine.engine.get_state()
car_city_engine.engine.stop()
car_city_engine.engine.get_state()
car_city_engine.tires.get_pressure()
car_city_engine.tires.pump()

print("=" * 40)

car_off_road_petrol = Vehicle("Jeep", petrol_engine, off_road_tire)
car_off_road_petrol.engine.start()
car_off_road_petrol.engine.get_state()
car_off_road_petrol.engine.stop()
car_off_road_petrol.engine.get_state()
car_off_road_petrol.tires.get_pressure()
car_off_road_petrol.tires.pump()