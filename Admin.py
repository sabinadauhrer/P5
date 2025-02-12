
import sys
import csv
from csv import DictReader
import math
import Address
import Person
import Customer
import User
import Database

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User

class Admin():
    def __init__(self, User):
        self.User=User
    def createDB():
        Database.createDB()
    def seedDB():
        Database.seedDB()
    def updateDB():
        Database.updateDB()
    def readDB():
        Database.readDB()
        