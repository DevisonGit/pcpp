class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 30  # Initial pressure

    def get_pressure(self):
        return self.pressure

    def pump(self):
        self.pressure += 5
        print(f"Tires pumped. Current pressure: {self.pressure}")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def start(self):
        if self.state == "off":
            self.state = "on"
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.state == "on":
            self.state = "off"
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def get_state(self):
        return self.state


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

    def display_info(self):
        print(f"Vehicle VIN: {self.VIN}")
        print(f"Engine Type: {self.engine.fuel_type}")
        print(f"Tires Size: {self.tires.size}")
        print(f"Engine State: {self.engine.get_state()}")
        print(f"Tires Pressure: {self.tires.get_pressure()}\n")


# Create two sets of tires
city_tires = Tires(size=15)
off_road_tires = Tires(size=18)

# Create two engines
electric_engine = Engine(fuel_type="Electric")
petrol_engine = Engine(fuel_type="Petrol")

# Instantiate two cars
city_car = Vehicle(VIN="ABC123", engine=electric_engine, tires=city_tires)
off_road_car = Vehicle(VIN="XYZ789", engine=petrol_engine, tires=off_road_tires)

# Display information about the cars
print("City Car Information:")
city_car.display_info()

print("Off-Road Car Information:")
off_road_car.display_info()

# Interact with the cars
city_car.engine.start()
city_car.tires.pump()

off_road_car.engine.start()
off_road_car.tires.pump()

# Display updated information about the cars
print("Updated City Car Information:")
city_car.display_info()

print("Updated Off-Road Car Information:")
off_road_car.display_info()
