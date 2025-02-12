import Person
Person=Person.Person

class User:
    def __init__(self, username, password, Person=Person):
        self.username=username
        self.password=password
        self.Person=Person

    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username=username
    def newUsername(self):
        self.username=input("Username:\n")
    
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password=password
    def newPassword(self):
        self.password=input("Password:\n")
            
    def getPerson(self):
        return self.Person
    def setPerson(self, Person=Person):
        self.Person=Person
    