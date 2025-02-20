
import Address
import Person
import Customer
import User
import Database
#import Session

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User

class Admin():
    def __init__(self, User):
        self._User=User
    
    def __str__(self):
        return f"({self._User})"
        
    def createDB():
        Database.createDB()
        
    def seedUser():
        Database.seedUser()
    def seedCustomer():
        Database.seedCustomer()
        
    def updateUser(column,value,ID):
        Database.updateUser(column,value,ID)
    def updateCustomer(column,value,ID):
        Database.updateCustomer(column,value,ID)
    def updateDB(column, value, ID):
        Database.updateDB(column, value, ID)
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
    def newCustomerP(country,zip,city,street,snumber,name,firstname,email,phone,iban,company):
        a1=Address(country,zip,city,street,snumber)
        p1=Person(name,firstname,email,phone,iban,a1)
        c1=Customer(company,p1)
        Database.seedCustomerComplete(c1,p1,a1)
    def deleteCustomerNP(name,firstname,email,phone,iban):
        Database.deleteCustomerN(name,firstname,email,phone,iban)
    def deleteCustomerIDP(ID):
        Database.deleteCustomerID(ID)
        
    def searchUserDBT():
        search=input("suche: \n")
        results=Database.searchUserDB(search)
        for row in results:
            print(row)
    def searchUserDBP(search):
        results=Database.searchUserDB(search)
        return results
    