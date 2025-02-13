
import Address
import Person
import Customer
import User

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User

import sqlite3

def createDB():
    db=sqlite3.connect('user.db')
    
    db.execute("""
        CREATE TABLE Address (
            ID INTEGER
            , country TEXT
            , zip TEXT
            , city TEXT
            , street TEXT
            , snumber TEXT
            , PRIMARY KEY(ID))""")

    db.execute("""
        CREATE TABLE Person (
            ID INTEGER
            , name TEXT
            , firstname TEXT
            , email TEXT
            , phone TEXT
            , iban TEXT
            , AddressID INTEGER
            , PRIMARY KEY(ID), FOREIGN KEY(AddressID) REFERENCES Address(ID))""")

    db.execute("""
        CREATE TABLE Customer (
            ID INTEGER
            , company TEXT
            , PersonID INTEGER
            , PRIMARY KEY(ID), FOREIGN KEY(PersonID) REFERENCES Person(ID))""")
    
    db.execute("""
        CREATE TABLE User (
            ID INTEGER
            , username TEXT
            , password TEXT
            , adminrole INTEGER
            , PersonID INTEGER
            , PRIMARY KEY(ID), FOREIGN KEY(PersonID) REFERENCES Person(ID))""")

    db.commit()
    db.close()
    seedroot()

def seedroot():
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("""INSERT INTO User (
        username,
        password,
        adminrole,
        PersonID
        ) VALUES (root, root, 1, ?);""", )
    db.commit()
    db.close()
    
def seedAddress(Address=Address):
    data=[Address.getCountry,Address.getZIP,Address.getCity,Address.getStreet,Address.setSnumber]
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("""INSERT INTO Address (
        country,
        zip,
        city,
        street,
        snumber
        ) VALUES (?, ?, ?, ?, ?);""", data)
    db.commit()
    db.close()
    
def seedPerson(Person=Person):
    data=[Person.getName,Person.getFirstname,Person.getEmail,Person.getPhone,Person.getIBAN]
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("""INSERT INTO Person (
        name,
        firstname,
        email,
        phone,
        iban,
        AddressID
        ) VALUES (?, ?, ?, ?, ?, ?);""", data)
    db.commit()
    db.close()
    
def seedUser(User=User):
    data=[User.getUsername,User.getPassword,0]
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("""INSERT INTO User (
        username,
        password,
        adminrole,
        PersonID
        ) VALUES (?, ?, ?, ?);""", data)
    db.commit()
    db.close()
    
def seedCustomer(Customer=Customer):
    data=[Customer.getCompany]
    db=sqlite3.connect('user.db')    
    cur=db.cursor()
    cur.execute("""INSERT INTO Customer (
        company,
        PersonID
        ) VALUES (?, ?);""", data)
    db.commit()
    db.close()
    
def updateDB():
    db=sqlite3.connect('user.db')
    
    db.commit()
    db.close()

def readDB():
    db=sqlite3.connect('user.db')
    
    db.commit()
    db.close()
