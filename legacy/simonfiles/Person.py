import Address
Address=Address.Address

class Person:
    def __init__(self, name,firstname,email,phone,iban, Address=Address):
        self._name=name
        self._firstname=firstname
        self._email=email
        self._phone=phone
        self._iban=iban
        self._Address=Address
        
    def __str__(self):
        return f"({self._name}, {self._firstname}, {self._email}, {self._phone}, {self._iban}, {self._Address})"
        
    def getName(self):
        return self._name
    def setName(self, name):
        self._name=name
    def newName(self):
        self.setName(input("Name:\n"))
            
    def getFirstname(self):
        return self._firstname
    def setFirstname(self, firstname):
        self._firstname=firstname
    def newFirstname(self):
        self.setFirstname(input("Firstname:\n"))
            
    def getEmail(self):
        return self._email
    def setEmail(self, email):
        self._email=email
    def newEmail(self):
        self.setEmail(input("E-Mail:\n"))
            
    def getPhone(self):
        return self._phone
    def setPhone(self, phone):
        self._phone=phone
    def newPhone(self):
        self.setPhone(input("Phonenumber:\n"))
            
    def getIBAN(self):
        return self._iban
    def setIBAN(self, iban):
        self._iban=iban
    def newIBAN(self):
        self.setIBAN(input("IBAN:\n"))
    
    def getAddress(self):
        return self._Address
    def setAddress(self, Address=Address):
        self._Address=Address
    def getCountry(self):
        return self._Address.getCountry()
    def setCountry(self, country):
        self._Address.setCountry(country)
    def getZIP(self):
        return self._Address.getZIP()
    def setZIP(self, zip):
        self._Address.setZIP(zip)
    def getCity(self):
        return self._Address.getCity()
    def setCity(self, city):
        self._Address.setCity(city)
    def getStreet(self):
        return self._Address.getStreet()
    def setStreet(self, street):
        self._Address.setStreet(street)
    def getSnumber(self):
        return self._Address.getSnumber()
    def setSnumber(self, snumber):
        self._Address.setSnumber(snumber)
    