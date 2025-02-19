
class Address:
    def __init__(self, country,zip,city,street,snumber):
        self.country=country
        self.zip=zip
        self.city=city
        self.street=street
        self.snumber=snumber
        
    def __str__(self):
        return f"({self.country}, {self.zip}, {self.city}, {self.street}, {self.snumber})"
    
    def getCountry(self):
        return self.country
    def setCountry(self, country):
        self.country=country
    def newCountry(self):
        self.setCountry(input("Country:\n"))
    
    def getZIP(self):
        return self.zip
    def setZIP(self, zip):
        self.zip=zip
    def newZIP(self):
        self.setZIP(input("ZIP:\n"))
    
    def getCity(self):
        return self.city
    def setCity(self, city):
        self.city=city
    def newCity(self):
        self.setCity(input("City:\n"))
    
    def getStreet(self):
        return self.street
    def setStreet(self, street):
        self.street=street
    def newStreet(self):
        self.setStreet(input("Street:\n"))
    
    def getSnumber(self):
        return self.snumber
    def setSnumber(self, snumber):
        self.snumber=snumber
    def newSnumber(self):
        self.setSnumber(input("Streetnumber:\n"))
