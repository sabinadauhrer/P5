import Person
Person=Person.Person

class Customer:
    def __init__(self, company, Person=Person):
        self._company=company
        self._Person=Person
        
    def __str__(self):
        return f"({self._company}, {self._Person})"

    def getCompany(self):
        return self._company
    def setCompany(self, company):
        self._company=company
    def newCompany(self):
        self.setCompany(input("Company:\n"))
        
    def getPerson(self):
        return self._Person
    def setPerson(self, Person=Person):
        self._Person=Person
    def getName(self):
        return self._Person.getName()
    def setName(self, name):
        self._Person.setName(name)
    def getFirstname(self):
        return self._Person.getFirstname()
    def setFirstname(self, firstname):
        self._Person.setFirstname(firstname)
    def getEmail(self):
        return self._Person.getEmail()
    def setEmail(self, email):
        self._Person.setEmail(email)
    def getPhone(self):
        return self._Person.getPhone()
    def setPhone(self, phone):
        self._Person.setPhone(phone)
    def getIBAN(self):
        return self._Person.getIBAN()
    def setIBAN(self, iban):
        self._Person.setIBAN(iban)
    