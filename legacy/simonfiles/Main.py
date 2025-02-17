
import sys
import csv
from csv import DictReader
import Address
import Person
import Customer
import User
import Admin
import Database
import Session

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User
Admin=Admin.Admin

def main():
    try:
        while True:
            choice=input("create Database (d): \nseed Database (s): \nupdate Database (u): \ncancel (c): \nlogin session (l)\n")
            if choice=='d'or choice=='s'or choice=='u'or choice=='c'or choice=='l':
                    break
        if choice=='d':
            Database.createDB()
        elif choice=='s':
            Database.seedUser()
        elif choice=='u':
            Database.updateUser()
        elif choice=='l':
            Session.loginUserT()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except TypeError as te:
        print(f"Error: {te}")
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
    
main()
