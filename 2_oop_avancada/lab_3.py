class Scanner:
    def scan(self):
        print("scan of Scanner")


class Printer:
    def print(self):
        print("print of class Printer")


class Fax:
    def send(self):
        print("send of class Fax")

    def print(self):
        print("print of class Fax")


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


spf = MFD_SPF()
sfp = MFD_SFP()

spf.scan()
spf.print()
spf.send()

sfp.scan()
sfp.print()
sfp.send()
