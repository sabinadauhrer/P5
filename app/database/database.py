import sqlite3
from app.models.user import User

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
    cur.execute("""
        INSERT INTO User (username, password, adminrole, PersonID)
        VALUES ('root', 'root', 1, ?)
    """)
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
    return cursor.lastrowid
    
    db.commit()
    db.close()
    
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