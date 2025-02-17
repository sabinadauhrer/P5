import app.models.Person as Person
Person=Person.Person

class Customer:
    def __init__(self, Person, company):
        self.Person=Person
        self.company=company
