
class Address:
    def __init__(self, country, zip, city, street, snumber):
        self.country=country
        self.zip=zip
        self.city=city
        self.street=street
        self.snumber=snumber
    
    def getUserName(self):
        return self.country
    def setUserName(self, country):
        self.country=country
    
    def getUserName(self):
        return self.zip
    def setUserName(self, zip):
        self.zip=zip
    
    def getUserName(self):
        return self.city
    def setUserName(self, city):
        self.city=city
    
    def getUserName(self):
        return self.street
    def setUserName(self, street):
        self.street=street
    
    def getUserName(self):
        return self.snumber
    def setUserName(self, snumber):
        self.snumber=snumber
    