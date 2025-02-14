
import sys
import csv
from csv import DictReader
import math
import app.models.address as Address
import app.models.person as Person
import app.models.customer as Customer
import app.models.user as User
import app.models.admin as Admin
import app.database.database as Database


def main():
    try:
        while True:
            choice=input("create Database (d): \nseed Database (s): \nupdate Database (u): \ncancel (c): \n")
            if choice=='d'or choice=='s'or choice=='u'or choice=='c':
                    break
        if choice=='d':
            Database.createDB()
        elif choice=='s':
            Database.seedDB()
        elif choice=='u':
            Database.updateDB()
        
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
    
main()
