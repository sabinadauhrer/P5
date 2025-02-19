
import Address
import Person
import Customer
import User
import Database
import Session

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User

class Admin():
    def __init__(self, User):
        self.User=User
    
    def __str__(self):
        return f"({self.User})"
        
    def createDB():
        Database.createDB()
    def seedUser():
        Database.seedUser()
    def seedCustomer():
        Database.seedCustomer()
    def updateDB():
        Database.updateUser()
    def newUserT():
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
        u1=User(
            input("Username:\n"),
            input("Password:\n"),
            p1
            )
        Database.seedUserComplete(u1,p1,a1)
    def newUserP(country,zip,city,street,snumber,name,firstname,email,phone,iban,username,password):
        a1=Address(country,zip,city,street,snumber)
        p1=Person(name,firstname,email,phone,iban,a1)
        u1=User(username,password,p1)
        Database.seedUserComplete(u1,p1,a1)
    def deleteUserNP(username):
        Database.deleteUserN(username)
    def deleteUserIDP(ID):
        Database.deleteUserID(ID)
    def deleteUserNT():
        username=input("username:\n")
        Database.deleteUserN(username)
        
    def newCustomerT():
        Session.newCustomerT()
    def newCustomerP(country,zip,city,street,snumber,name,firstname,email,phone,iban,company):
        Session.newCustomerP(country,zip,city,street,snumber,name,firstname,email,phone,iban,company)
    def deleteCustomerNP(name,firstname,email,phone,iban):
        Session.deleteCustomerNP(name,firstname,email,phone,iban)
    def deleteCustomerIDP(ID):
        Session.deleteCustomerIDP(ID)