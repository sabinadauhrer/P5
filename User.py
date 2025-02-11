import Person
Person=Person.Person

class User:
    def __init__(self, Person, username, password):
        self.Person=Person
        self.username=username
        self.password=password
