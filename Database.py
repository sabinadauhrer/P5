
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
            , PRIMARY KEY(ID))""")

    db.execute("""
        CREATE TABLE Customer (
            ID INTEGER
            , company TEXT
            , PersonID INTEGER
            , PRIMARY KEY(ID))""")
    
    db.execute("""
        CREATE TABLE User (
            ID INTEGER
            , username TEXT
            , password TEXT
            , adminrole INTEGER
            , PersonID INTEGER
            , PRIMARY KEY(ID))""")

    db.commit()
    db.close()

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
    
def seedDB():
    db=sqlite3.connect('user.db')
    
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
