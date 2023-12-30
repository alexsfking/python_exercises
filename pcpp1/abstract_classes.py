'''
Estimated time
    40 minutes

Level of difficulty
    Medium

Objectives
    Creation of abstract classes and abstract methods;
    multiple inheritance of abstract classes;
    overriding abstract methods;
    delivering multiple child classes.

Scenario
    You are about to create a multifunction device (MFD) that can scan and print
    documents;
    the system consists of a scanner and a printer;
    your task is to create blueprints for it and deliver the implementations;
    create an abstract class representing a scanner that enforces the following
    methods:
        scan_document – returns a string indicating that the document has been scanned;
        get_scanner_status – returns information about the scanner (max. resolution,
        serial number)
    Create an abstract class representing a printer that enforces the following
    methods:
        print_document – returns a string indicating that the document has been printed;
        get_printer_status – returns information about the printer (max. resolution,
        serial number)
    Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible
    for scanning and printing:
        MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so
        device capabilities (resolution) should be low;
        MFD2 – should be a medium-priced device allowing additional operations like
        printing operation history, and the resolution is better than the lower-priced
        device;
        MFD3 – should be a premium device allowing additional operations like printing
        operation history and fax machine.
    Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices
    should be capable of serving generic feature sets.
'''

import abc

class Scanner_abstract(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer_abstract(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Printer_abstract, Scanner_abstract):
    def __init__(self) -> None:
        self.__scanner_value = "Cheap"
        self.__printer_value = "Cheap"
        self.__scanner_available = "Available"
        self.__printer_available = "Available"

    def scan_document(self):
        return f"{self.__scanner_value} scanner"
    
    def get_scanner_status(self):
        return f"The scanner is {self.__scanner_available}"
    
    def print_document(self):
        return f"{self.__printer_value} printer"
    
    def get_printer_status(self):
        return f"The printer is {self.__printer_available}"
    
mfd1 = MFD1()
print(mfd1.scan_document())
print(mfd1.get_scanner_status())
print(mfd1.print_document())
print(mfd1.get_printer_status())