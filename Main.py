
import sys
import csv
from csv import DictReader
import math
import User
import Admin
import Address
import Database
import Seed
import UpdateDB

User=User.User
Admin=Admin.Admin
Address=Address.Address

def createDB():
    try:
        Database.call(["python", "Database.py"])
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


def main():
    try:
        while True:
            choice=input("create Database (d): \nseed Database (s): \nupdate Database (u): \ncancel (c):")
            if choice=='d' or choice=='s'or choice=='u'or choice=='c':
                    break
        if choice=='d':
            createDB()
        elif choice=='s':
            seedDB()
        elif choice=='u':
            updateDB()
            
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
        
main()
