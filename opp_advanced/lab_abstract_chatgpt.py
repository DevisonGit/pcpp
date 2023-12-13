from abc import ABC, abstractmethod

# Abstract Scanner Class
class Scanner(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        pass

    @abstractmethod
    def get_scanner_status(self) -> str:
        pass

# Abstract Printer Class
class Printer(ABC):
    @abstractmethod
    def print_document(self) -> str:
        pass

    @abstractmethod
    def get_printer_status(self) -> str:
        pass

# Multifunction Device (MFD) Base Class
class MFD(Scanner, Printer, ABC):
    def __init__(self, resolution: int, serial_number: str):
        self.resolution = resolution
        self.serial_number = serial_number

    def get_mfd_status(self) -> str:
        return f"MFD Status: Resolution {self.resolution}, Serial Number {self.serial_number}"

# MFD1 - Cheap Device
class MFD1(MFD):
    def __init__(self):
        super().__init__(resolution=300, serial_number="MFD1")

    def scan_document(self) -> str:
        return "Document scanned with MFD1"

    def print_document(self) -> str:
        return "Document printed with MFD1"

    def get_scanner_status(self) -> str:
        return f"Scanner Status: Resolution {self.resolution}, Serial Number {self.serial_number}"

    def get_printer_status(self) -> str:
        return f"Printer Status: Resolution {self.resolution}, Serial Number {self.serial_number}"


# MFD2 - Medium-Priced Device
class MFD2(MFD):
    def __init__(self):
        super().__init__(resolution=600, serial_number="MFD2")

    def scan_document(self) -> str:
        return "Document scanned with MFD2"

    def print_document(self) -> str:
        return "Document printed with MFD2"

    def print_operation_history(self) -> str:
        return "Printing operation history available with MFD2"

    def get_scanner_status(self) -> str:
        return f"Scanner Status: Resolution {self.resolution}, Serial Number {self.serial_number}"

    def get_printer_status(self) -> str:
        return f"Printer Status: Resolution {self.resolution}, Serial Number {self.serial_number}"


# MFD3 - Premium Device
class MFD3(MFD):
    def __init__(self):
        super().__init__(resolution=1200, serial_number="MFD3")

    def scan_document(self) -> str:
        return "Document scanned with MFD3"

    def print_document(self) -> str:
        return "Document printed with MFD3"

    def print_operation_history(self) -> str:
        return "Printing operation history available with MFD3"

    def fax(self) -> str:
        return "Faxing functionality available with MFD3"

    def get_scanner_status(self) -> str:
        return f"Scanner Status: Resolution {self.resolution}, Serial Number {self.serial_number}"

    def get_printer_status(self) -> str:
        return f"Printer Status: Resolution {self.resolution}, Serial Number {self.serial_number}"


# Instantiate MFD1, MFD2, and MFD3
mfd1 = MFD1()
mfd2 = MFD2()
mfd3 = MFD3()

# Demonstrate abilities
print(mfd1.scan_document())
print(mfd1.print_document())
print(mfd1.get_mfd_status())

print("\n" + "="*30 + "\n")

print(mfd2.scan_document())
print(mfd2.print_document())
print(mfd2.print_operation_history())
print(mfd2.get_mfd_status())

print("\n" + "="*30 + "\n")

print(mfd3.scan_document())
print(mfd3.print_document())
print(mfd3.print_operation_history())
print(mfd3.fax())
print(mfd3.get_mfd_status())
