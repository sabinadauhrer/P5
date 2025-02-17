import app.models.Address as Address
import app.models.Person as Person
import app.models.Customer as Customer
import app.models.User as User
import app.Database as Database

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User

class Admin():
    def __init__(self, User, adminrole):
        self.User=User
        self.adminrole=adminrole
    def createDB():
        Database.createDB()
    def seedDB():
        Database.seedDB()
    def updateDB():
        Database.updateDB()
    def readDB():
        Database.readDB()
        