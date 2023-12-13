import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MDF1(Scanner, Printer):
    def scan_document(self, document):
        return "{} the document has been scanned".format(document)
    
    def get_scanner_status(self):
        return "resolution: low"
    
    def print_document(self, document):
        return "{} the document has been printed".format(document)
    
    def get_printer_status(self):
        return "resolution: low"


class MDF2(Scanner, Printer):
    def __init__(self) -> None:
        self.history = []

    def scan_document(self, document):
        return "{} the document has been scanned".format(document)
    
    def get_scanner_status(self):
        return "resolution: medium"
    
    def print_document(self, document):
        self.history.append(document)
        return "{} the document has been printed".format(document)
    
    def get_printer_status(self):
        return "resolution: medium"
    
    def history_print(self):
        return self.history


class MDF3(Scanner, Printer):
    def __init__(self) -> None:
        self.history = []

    def scan_document(self, document):
        return "{} the document has been scanned".format(document)
    
    def get_scanner_status(self):
        return "resolution: premium"
    
    def print_document(self, document):
        self.history.append(document)
        return "{} the document has been printed".format(document)
    
    def get_printer_status(self):
        return "resolution: premium"
    
    def history_print(self):
        return self.history
    
    def fax_machine(self):
        return "fax machine"

print("MDF1")
mdf1 = MDF1()
print(mdf1.scan_document('mydoc'))
print(mdf1.get_scanner_status())
print(mdf1.print_document("mydoc"))
print(mdf1.get_printer_status())

print("\nMDF2")
mdf2 = MDF2()
print(mdf2.scan_document('mydoc'))
print(mdf2.get_scanner_status())
print(mdf2.print_document("mydoc"))
print(mdf2.get_printer_status())
print(mdf2.print_document("mydoc_v2"))
print(mdf2.get_printer_status())
print(mdf2.history_print())

print("\nMDF3")
mdf3 = MDF3()
print(mdf3.scan_document('mydoc'))
print(mdf3.get_scanner_status())
print(mdf3.print_document("mydoc"))
print(mdf3.get_printer_status())
print(mdf3.print_document("mydoc_v2"))
print(mdf3.get_printer_status())
print(mdf3.history_print())
print(mdf3.fax_machine())
