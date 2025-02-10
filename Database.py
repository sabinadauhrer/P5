import sqlite3

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
    CREATE TABLE User (
        ID INTEGER
        , username TEXT
        , name TEXT
        , firstname TEXT
        , email TEXT
        , phone TEXT
        , iban TEXT
        , AddressID INTEGER
        , PRIMARY KEY(ID))""")

db.execute("""
    CREATE TABLE Admin (
        ID INTEGER
        , UserID INTEGER
        , PRIMARY KEY(ID))""")
