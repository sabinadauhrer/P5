
class Address:
    def __init__(self, country, zip, city, street, snumber):
        self.country=country
        self.zip=zip
        self.city=city
        self.street=street
        self.snumber=snumber
    
    def getCountry(self):
        return self.country
    def setCountry(self, country):
        self.country=country
    
    def getZIP(self):
        return self.zip
    def setZIP(self, zip):
        self.zip=zip
    
    def getCity(self):
        return self.city
    def setCity(self, city):
        self.city=city
    
    def getStreet(self):
        return self.street
    def setStreet(self, street):
        self.street=street
    
    def getSnumber(self):
        return self.snumber
    def setSnumber(self, snumber):
        self.snumber=snumber
    