import Address
import Person
import Customer
#import Database

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer

class User:
    def __init__(self, username,password, Person=Person):
        self.username=username
        self.password=password
        self.Person=Person
        
    def __str__(self):
        return f"({self.username}, {self.Person})"

    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username=username
    def newUsername(self):
        self.setUsername(input("Username:\n"))
    
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password=password
    def newPassword(self):
        self.setPassword(input("Password:\n"))
            
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
    
"""    def newCustomerT():
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
        Database.seedCustomerComplete(c1,p1,a1)
    
    def newCustomerP(country,zip,city,street,snumber,name,firstname,email,phone,iban,company):
        a1=Address(country,zip,city,street,snumber)
        p1=Person(name,firstname,email,phone,iban,a1)
        c1=Customer(company,p1)
        Database.seedCustomerComplete(c1,p1,a1)
        
    def deleteCustomerP(name,firstname,email,phone,iban):
        Database.deleteCustomer(name,firstname,email,phone,iban)
        """