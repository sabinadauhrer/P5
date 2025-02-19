
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
    if vuser:
        adata=vuser['Address']
        pdata=vuser['Person']
        udata=vuser['User']
        admincheck=vuser['Admin']
        a1=Address(*adata)
        p1=Person(*pdata,a1)
        u1=User(udata[0],udata[1],p1)
        if admincheck==1:
            r1=Admin(u1)
            print(a1,p1,u1,r1)
        else:
            print(a1,p1,u1)
    else:
        print("Invalid username or password")
def loginUserP(usernamep, passwordp):
    username=usernamep
    password=passwordp
    vuser=Database.readLoginDB(username,password)
    if vuser:
        adata=vuser['Address']
        pdata=vuser['Person']
        udata=vuser['User']
        admincheck=vuser['Admin']
        a1=Address(*adata)
        p1=Person(*pdata,a1)
        u1=User(udata[0],udata[1],p1)
        if admincheck==1:
            r1=Admin(u1)
            return a1,p1,u1,r1
        else:
            return a1,p1,u1
    else:
        return
# --- User Funktionen ---
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
    Database.seedCustomerComplete(c1,p1,a1)
def newCustomerP(country,zip,city,street,snumber,name,firstname,email,phone,iban,company):
    a1=Address(country,zip,city,street,snumber)
    p1=Person(name,firstname,email,phone,iban,a1)
    c1=Customer(company,p1)
    Database.seedCustomerComplete(c1,p1,a1)
        
def deleteCustomerNP(name,firstname,email,phone,iban):
    Database.deleteCustomerN(name,firstname,email,phone,iban)
def deleteCustomerIDP(ID):
    Database.deleteCustomerID(ID)      
    
def searchCustomerDBT():
    search=input("suche: \n")
    results=Database.searchCustomerDB(search)
    for row in results:
        print(row)
def searchCustomerDBP(search):
    results=Database.searchCustomerDB(search)
    return results
