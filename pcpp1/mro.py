class Scanner:
    def scan(self):
        print('Scan from Scanner class')

class Printer:
    def print(self):
        print('Print from Printer class')
        
class Fax():
    def send(self):
        print('Send from Fax class')
        
    def print(self):
        print('Print from Fax class')
        
class MFD_SPF(Scanner, Printer, Fax):
    pass
    
class MFD_SFP(Scanner, Fax, Printer):
    pass

mfd_spf = MFD_SPF()
mfd_spf.scan()
mfd_spf.print()
mfd_spf.send()
mfd_sfp = MFD_SFP()
mfd_sfp.scan()
mfd_sfp.print()
mfd_sfp.send()