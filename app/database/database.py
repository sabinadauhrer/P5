import sqlite3
import config
from app.models.user import User
from app.models.hash import *

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
    adata = ['root', 'root', 'root', 'root', 'root']
    db = sqlite3.connect('user.db')
    cur = db.cursor()
    cur.execute("""INSERT INTO Address (
        country,
        zip,
        city,
        street,
        snumber
        ) VALUES (?, ?, ?, ?, ?);""", adata)
    db.commit()
    db.close()
    
    db = sqlite3.connect('user.db')
    cur = db.cursor()
    cur.execute(
        "SELECT id FROM Address WHERE zip = ? AND street = ? AND snumber = ?"
        , ('root', 'root', 'root'))
    AddressID = cur.fetchone()[0]
    pdata = ['root', 'root', config.root_email, 'root', 'root', AddressID]
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
    
    db = sqlite3.connect('user.db')
    cur = db.cursor()
    cur.execute(
        "SELECT id FROM Person WHERE email = ? AND phone = ? AND iban = ?"
        , ('root', 'root', 'root'))
    PersonID = cur.fetchone()[0]
    
    hashed_password = hash_password(config.root_password)
    udata = [config.root_username, hashed_password, 1, PersonID]
    cur.execute("""INSERT INTO User (
        username,
        password,
        adminrole,
        PersonID
        ) VALUES (?, ?, ?, ?);""", udata)
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

def save_user_to_db(user):
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    
    # Adresse hinzufügen
    cursor.execute("""
        INSERT INTO Address (country, zip, city, street, snumber)
        VALUES (?, ?, ?, ?, ?)""", (user.person.address.country, user.person.address.zip, user.person.address.city, user.person.address.street, user.person.address.snumber))
    address_id = cursor.lastrowid
    
    # Person hinzufügen
    cursor.execute("""
        INSERT INTO Person (name, firstname, email, phone, iban, AddressID)
        VALUES (?, ?, ?, ?, ?, ?)""", (user.person.name, user.person.firstname, user.person.email, user.person.phone, user.person.iban, address_id))
    person_id = cursor.lastrowid
    
    # Benutzer hinzufügen
    cursor.execute("""
    INSERT INTO User (username, password, PersonID, adminrole)
    VALUES (?, ?, ?, ?)""", (user.username, user.password, person_id, user.adminrole))
    db.commit()
    db.close()

    return cursor.lastrowid

    return user_id

def get_user_by_username(username):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return User(
            id=row[0],  # Setze das id-Attribut
            person=None,  # Sie können hier die Person-Details hinzufügen, wenn nötig
            username=row[1],
            password=row[2],
            adminrole=row[3]
        )
    return None

def get_all_users():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT User.ID, User.username, User.password, User.adminrole, Person.name, Person.firstname, Person.email, Person.phone, Person.iban, Address.country, Address.zip, Address.city, Address.street, Address.snumber
        FROM User
        JOIN Person ON User.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
    """)
    rows = cursor.fetchall()
    conn.close()
    
    users = []
    for row in rows:
        user = {
            'id': row[0],
            'username': row[1],
            'password': row[2],
            'adminrole': row[3],
            'name': row[4],
            'firstname': row[5],
            'email': row[6],
            'phone': row[7],
            'iban': row[8],
            'country': row[9],
            'zip': row[10],
            'city': row[11],
            'street': row[12],
            'snumber': row[13]
        }
        users.append(user)
    
    return users