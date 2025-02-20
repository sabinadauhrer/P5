import app.models.person as Person
Person = Person.Person

class Customer:
    def __init__(self, person, company):
        self.person = person
        self.company = company