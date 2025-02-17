
import sys
import csv
from csv import DictReader
import math
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

"""
def createDB():
    try:
        Database.call(["python", "Database.py", "createDB()"])
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])

def seedDB():
    try:
        Seed.call(["python", "Seed.py"])
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])

def updateDB():
    try:
        UpdateDB.call(["python", "UpdateDB.py"])
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
        
"""

def main():
    try:
        while True:
            choice=input("create Database (d): \nseed Database (s): \nupdate Database (u): \ncancel (c): \n")
            if choice=='d'or choice=='s'or choice=='u'or choice=='c':
                    break
        if choice=='d':
            Database.createDB()
        elif choice=='s':
            Database.seedUser()
        elif choice=='u':
            Database.updateDB()
            
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
        print(u1)
        
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
    
main()
