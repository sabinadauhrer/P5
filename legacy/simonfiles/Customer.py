import Person
Person=Person.Person

class Customer:
    def __init__(self, company, Person=Person):
        self.company=company
        self.Person=Person
        
    def __str__(self):
        return f"({self.company}, {self.Person})"

    def getCompany(self):
        return self.company
    def setCompany(self, company):
        self.company=company
    def newCompany(self):
        self.setCompany(input("Company:\n"))
        
    def getPerson(self):
        return self.Person
    def setPerson(self, Person=Person):
        self.Person=Person
    def getName(self):
        return self.Person.getName
    def setName(self, name):
        self.Person.setName=name
    def getFirstname(self):
        return self.Person.getFirstname
    def setFirstname(self, firstname):
        self.Person.setFirstname=firstname
    def getEmail(self):
        return self.Person.getEmail
    def setEmail(self, email):
        self.Person.setEmail=email
    def getPhone(self):
        return self.Person.getPhone
    def setPhone(self, phone):
        self.Person.setPhone=phone
    def getIBAN(self):
        return self.Person.getIBAN
    def setIBAN(self, iban):
        self.Person.setIBAN=iban
    