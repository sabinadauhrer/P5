import Address
Address=Address.Address

class Person:
    def __init__(self, name,firstname,email,phone,iban, Address=Address):
        self.name=name
        self.firstname=firstname
        self.email=email
        self.phone=phone
        self.iban=iban
        self.Address=Address
        
    def __str__(self):
        return f"({self.name}, {self.firstname}, {self.email}, {self.phone}, {self.iban}, {self.Address})"
        
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def newName(self):
        self.setName(input("Name:\n"))
            
    def getFirstname(self):
        return self.firstname
    def setFirstname(self, firstname):
        self.firstname=firstname
    def newFirstname(self):
        self.setFirstname(input("Firstname:\n"))
            
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email=email
    def newEmail(self):
        self.setEmail(input("E-Mail:\n"))
            
    def getPhone(self):
        return self.phone
    def setPhone(self, phone):
        self.phone=phone
    def newPhone(self):
        self.setPhone(input("Phonenumber:\n"))
            
    def getIBAN(self):
        return self.iban
    def setIBAN(self, iban):
        self.iban=iban
    def newIBAN(self):
        self.setIBAN(input("IBAN:\n"))
    
    def getAddress(self):
        return self.Address
    def setAddress(self, Address=Address):
        self.Address=Address
    def getCountry(self):
        return self.Address.getCountry
    def setCountry(self, country):
        self.Address.setCountry=country
    def getZIP(self):
        return self.Address.getZIP
    def setZIP(self, zip):
        self.Address.setZIP=zip
    def getCity(self):
        return self.Address.getCity
    def setCity(self, city):
        self.Address.setCity=city
    def getStreet(self):
        return self.Address.getStreet
    def setStreet(self, street):
        self.Address.setStreet=street
    def getSnumber(self):
        return self.Address.getSnumber
    def setSnumber(self, snumber):
        self.Address.setSnumber=snumber
    