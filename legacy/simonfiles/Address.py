
class Address:
    def __init__(self, country,zip,city,street,snumber):
        self._country=country
        self._zip=zip
        self._city=city
        self._street=street
        self._snumber=snumber
        
    def __str__(self):
        return f"({self._country}, {self._zip}, {self._city}, {self._street}, {self._snumber})"
    
    def getCountry(self):
        return self._country
    def setCountry(self, country):
        self._country=country
    def newCountry(self):
        self.setCountry(input("Country:\n"))
    
    def getZIP(self):
        return self._zip
    def setZIP(self, zip):
        self._zip=zip
    def newZIP(self):
        self.setZIP(input("ZIP:\n"))
    
    def getCity(self):
        return self._city
    def setCity(self, city):
        self._city=city
    def newCity(self):
        self.setCity(input("City:\n"))
    
    def getStreet(self):
        return self._street
    def setStreet(self, street):
        self._street=street
    def newStreet(self):
        self.setStreet(input("Street:\n"))
    
    def getSnumber(self):
        return self._snumber
    def setSnumber(self, snumber):
        self._snumber=snumber
    def newSnumber(self):
        self.setSnumber(input("Streetnumber:\n"))
