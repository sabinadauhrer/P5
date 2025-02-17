
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
    