
import sys
import csv
from csv import DictReader
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

def main():
    try:
        
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
        """
        u1=User(
            input("Username:\n"),
            input("Password:\n"),
            p1=Person(
                input("Name:\n"),
                input("Firstname:\n"),
                input("E-Mail:\n"),
                input("Phonenumber:\n"),
                input("IBAN:\n"),
                a1=Address(
                    input("Country:\n"),
                    input("ZIP:\n"),
                    input("City:\n"),
                    input("Street:\n"),
                    input("Streetnumber:\n")
                    )
                )
            )
        print(u1)
        """
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except TypeError as te:
        print(f"Error: {te}")
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
    
main()
