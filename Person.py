import Address
Address=Address.Address

class Person:
    def __init__(self, name, firstname, email, phone, iban, Address=Address):
        self.name=name
        self.firstname=firstname
        self.email=email
        self.phone=phone
        self.iban=iban
        self.Address=Address
        
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
            
    def getFirstname(self):
        return self.firstname
    def setFirstname(self, firstname):
        self.firstname=firstname
            
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email=email
            
    def getPhone(self):
        return self.phone
    def setPhone(self, phone):
        self.phone=phone
            
    def getIBAN(self):
        return self.iban
    def setIBAN(self, iban):
        self.iban=iban
    