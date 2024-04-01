import abc


class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Print(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MDF1(Scanner, Print):
    def scan_document(self):
        return "the document has been scanned"

    def get_scanner_status(self):
        return f"resolution 1000\nSerial 1234"

    def print_document(self):
        return "the document has been printed"

    def get_printer_status(self):
        return f"resolution 1000\nSerial 4321"


class MDF2(Scanner, Print):
    scans = 0
    prints = 0

    def scan_document(self):
        MDF2.scans += 1
        return "the document has been scanned"

    def get_scanner_status(self):
        return f"resolution 5000\nSerial 5678"

    def print_document(self):
        MDF2.prints += 1
        return "the document has been printed"

    def get_printer_status(self):
        return f"resolution 5000\nSerial 8765"

    @classmethod
    def print_history(cls):
        return f"history operation:\nScan:{cls.scans}\nPrint:{cls.prints}"


class MDF3(Scanner, Print):
    scans = 0
    prints = 0
    fax = 0

    def scan_document(self):
        MDF3.scans += 1
        return "the document has been scanned"

    def get_scanner_status(self):
        return f"resolution 10000\nSerial 9101"

    def print_document(self):
        MDF3.prints += 1
        return "the document has been printed"

    def get_printer_status(self):
        return f"resolution 10000\nSerial 1019"

    @staticmethod
    def print_fax():
        MDF3.fax += 1
        return "the fax has been send"

    @staticmethod
    def get_fax_status():
        return f"resolution 10000\nSerial 1019"

    @classmethod
    def print_history(cls):
        return f"history operation:\nScan:{cls.scans}\nPrint:{cls.prints}\nFax:{cls.fax}"


mdf_1 = MDF1()
print(mdf_1.print_document())
print(mdf_1.scan_document())
print(mdf_1.get_printer_status())
print(mdf_1.get_scanner_status())

print("*" * 20)

mdf_2 = MDF2()
print(mdf_2.print_document())
print(mdf_2.scan_document())
print(mdf_2.get_printer_status())
print(mdf_2.get_scanner_status())
print(mdf_2.print_history())

print("*" * 20)

mdf_3 = MDF3()
print(mdf_3.print_document())
print(mdf_3.scan_document())
print(mdf_3.print_fax())
print(mdf_3.get_printer_status())
print(mdf_3.get_scanner_status())
print(mdf_3.get_fax_status())
print(mdf_3.print_history())


