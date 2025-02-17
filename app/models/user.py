import app.models.person as Person
Person=Person.Person

class User:
    def __init__(self, id, person, username, password, adminrole=0):
        self.id = id
        self.person = person
        self.username = username
        self.password = password
        self.adminrole = adminrole