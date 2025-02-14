
import Address
import Person
import Customer
import User
import Admin

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User
Admin=Admin.Admin

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
    adata=['root','root','root','root','root']
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("""INSERT INTO Address (
        country,
        zip,
        city,
        street,
        snumber
        ) VALUES (?, ?, ?, ?, ?);""", adata)
    db.commit()
    db.close()
    
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Address WHERE zip = ? AND street = ? AND snumber = ?"
        , ('root','root','root'))
    AddressID=cur.fetchone()
    AddressID=AddressID[0]
    pdata=['root','root','root','root','root',AddressID]
    cur.execute("""INSERT INTO Person (
        name,
        firstname,
        email,
        phone,
        iban,
        AddressID
        ) VALUES (?, ?, ?, ?, ?, ?);""", pdata)
    db.commit()
    db.close()
    
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Person WHERE email = ? AND phone = ? AND iban = ?"
        , ('root','root','root'))
    PersonID=cur.fetchone()
    PersonID=PersonID[0]
    udata=['root','root',1,PersonID]
    cur.execute("""INSERT INTO User (
        username,
        password,
        adminrole,
        PersonID
        ) VALUES (?, ?, ?, ?);""", udata)
    db.commit()
    db.close()
    
def seedAddress(Address=Address):
    data=[Address.getCountry,Address.getZIP,Address.getCity,Address.getStreet,Address.getSnumber]
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
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Address WHERE zip = ? AND street = ? AND snumber = ?"
        , (Person.getAddress,Person.getStreet,Person.getSnumber))
    AddressID=cur.fetchone()
    if AddressID:
        AddressID=AddressID[0]
        data=[Person.getName,Person.getFirstname,Person.getEmail,Person.getPhone,Person.getIBAN,AddressID]
        cur.execute("""INSERT INTO Person (
            name,
            firstname,
            email,
            phone,
            iban,
            AddressID
            ) VALUES (?, ?, ?, ?, ?, ?);""", data)
        db.commit()
    else:
        print(f"No address found with the provided data for {Person.getAddress()}, {Person.getStreet()}, {Person.getSnumber()}.")
    db.close()
    
def seedUser(User=User):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Person WHERE email = ? AND phone = ? AND iban = ?"
        , (User.getEmail,User.getPhone,User.getIBAN))
    PersonID=cur.fetchone()
    if PersonID:
        PersonID=PersonID[0]
        data=[User.getUsername,User.getPassword,0,PersonID]
        cur.execute("""INSERT INTO User (
            username,
            password,
            adminrole,
            PersonID
            ) VALUES (?, ?, ?, ?);""", data)
        db.commit()
    else:
        print(f"No address found with the provided data for {User.getEmail()}, {User.getPhone()}, {User.getIBAN()}.")
    db.close()
    
def seedUserComplete(User=User,Person=Person,Address=Address):
    seedAddress(Address)
    seedPerson(Person)
    seedUser(User)
    
def seedCustomer(Customer=Customer):
    db=sqlite3.connect('user.db')    
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Person WHERE email = ? AND phone = ? AND iban = ?"
        , (Customer.getEmail,Customer.getPhone,Customer.getIBAN))
    PersonID=cur.fetchone()
    if PersonID:
        PersonID=PersonID[0]
        data=[Customer.getCompany,PersonID]
        cur.execute("""INSERT INTO Customer (
            company,
            PersonID
            ) VALUES (?, ?);""", data)
        db.commit()
    else:
        print(f"No address found with the provided data for {Customer.getEmail()}, {Customer.getPhone()}, {Customer.getIBAN()}.")
    db.close()

def seedCustomerComplete(Customer=Customer,Person=Person,Address=Address):
    seedAddress(Address)
    seedPerson(Person)
    seedCustomer(Customer)
    
def updateUser():
    db=sqlite3.connect('user.db')
    
    db.commit()
    db.close()
    
def updateCustomer():
    db=sqlite3.connect('user.db')
    
    db.commit()
    db.close()

def readLoginDB(username,password):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("SELECT PersonID FROM User WHERE username = ? AND password = ?",(username,password))
    PersonID=cur.fetchone()
    if PersonID:
        PersonID=PersonID[0]
        cur.execute(
            "SELECT AddressID FROM Person WHERE ID = ?"
            , (PersonID))
        AddressID=cur.fetchone()
        if AddressID:
            AddressID=AddressID[0]
            cur.execute(
            "SELECT * FROM Address WHERE ID = ?"
            , (AddressID))
            adata=cur.fetchall()
            a1=Address.Address(adata)
        else:
            print(f"No address found with the provided data for {AddressID}.")
        cur.execute(
        "SELECT * FROM Person WHERE ID = ?"
        , (PersonID))
        pdata=cur.fetchall()
        p1=Person.Person(pdata,a1)
        cur.execute(
        "SELECT username AND password FROM User WHERE username = ? AND password = ?"
        , (username,password))
        udata=cur.fetchall()
        u1=User.User(udata,p1)
        cur.execute(
        "SELECT adminrole FROM User WHERE username = ? AND password = ?"
        , (username,password))
        admincheck=cur.fetchone()
        admincheck=admincheck[0]
        if admincheck==1:
            r1=Admin.Admin(u1)
            return a1,p1,r1
        else:
            return a1,p1,u1
    else:
        print(f"No address found with the provided data for {username,password}.")
    db.commit()
    db.close()
    