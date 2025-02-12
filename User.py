import Address
import Person
import Customer
Address=Address.Address
Person=Person.Person
Customer=Customer.Customer

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
    
    def newCustomer():
        a1=Address(
            input("Country:\n"),
            input("ZIP:\n"),
            input("City:\n"),
            input("Street:\n"),
            input("Streetnumber:\n")
            )
        p1=Person(
            input("Name:\n"),
            input("Firstname:\n"),
            input("E-Mail:\n"),
            input("Phonenumber:\n"),
            input("IBAN:\n"),
            a1
            )
        c1=Customer(
            input("Company:\n"),
            p1
            )
        return c1,p1,a1
    