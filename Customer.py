import Person
Person=Person.Person

class Customer:
    def __init__(self, company, Person=Person):
        self.company=company
        self.Person=Person

    def getCompany(self):
        return self.company
    def setCompany(self, company):
        self.company=company
    def newCompany(self):
        self.company=input("Company:\n")
        
    def getPerson(self):
        return self.Person
    def setPerson(self, Person=Person):
        self.Person=Person
    