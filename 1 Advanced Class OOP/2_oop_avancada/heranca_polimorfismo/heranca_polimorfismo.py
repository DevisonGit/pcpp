class Device:
    def turn_on(self):
        print("The device was turned of")


class Radio(Device):
    pass


class PortableRadio(Device):
    def turn_on(self):
        print("PortableRadio type object was turned on")


class TvSet(Device):
    def turn_on(self):
        print("TvSet type object was turned on")


device = Device()
radio = Radio()
portable_radio = PortableRadio()
tv_set = TvSet()

for element in (device, radio, portable_radio, tv_set):
    element.turn_on()
