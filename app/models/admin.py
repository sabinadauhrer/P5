import app.models.address as Address
import app.models.person as Person
import app.models.customer as Customer
import app.models.user as User
import app.database as Database

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
        