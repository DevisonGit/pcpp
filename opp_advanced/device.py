class Device():
    def turn_on(self):
        print("The device was turned on")


# inheritance
class Radio(Device):
    pass


# inheritance
class PortableRadio(Device):
    def turn_on(self):
        print("PortableRadio type was turned on")


# inheritance
class TvSet(Device):
    def turn_on(self):
        print("TvSet type was turned on")

device = Device()
radio = Radio()
portable_radio = PortableRadio()
tvset = TvSet()

# polymorphism
for element in (device, radio, portable_radio, tvset):
    element.turn_on()
