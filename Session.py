
import Address
import Person
import Customer
import User
import Admin
import Database

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User
Admin=Admin.Admin

def loginUserT():
    username=input("username:\n")
    password=input("password:\n")
    vuser=Database.readLoginDB(username,password)
    a1=vuser[0]
    p1=vuser[0]
    
    
def loginUserP(usernamep, passwordp):
    username=usernamep
    password=passwordp
    Database.readLoginDB(username,password)
    