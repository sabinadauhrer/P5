import Person
Person=Person.Person

class User:
    def __init__(self, username, password, Person=Person):
        self.username=username
        self.password=password
        self.Person=Person

    def getUserName(self):
        return self.username
    def setUserName(self, username):
        self.username=username
    
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password=password
        