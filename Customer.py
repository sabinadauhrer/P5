import Person
Person=Person.Person

class Customer:
    def __init__(self, Person, company):
        self.Person=Person
        self.company=company

    def getCompany(self):
        return self.company
    def setCompany(self, company):
        self.company=company
        