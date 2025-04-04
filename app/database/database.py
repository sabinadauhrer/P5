import sqlite3
import config
from app.models.user import User
from app.models.person import Person
from app.models.address import Address
from app.models.hash import hash_password
from app.models.customer import Customer
from flask import session

def createDB():
    db = sqlite3.connect('user.db')
    
    db.execute("""
        CREATE TABLE Address (
            ID INTEGER PRIMARY KEY,
            country TEXT,
            zip TEXT,
            city TEXT,
            street TEXT,
            snumber TEXT
        )""")

    db.execute("""
        CREATE TABLE Person (
            ID INTEGER PRIMARY KEY,
            name TEXT,
            firstname TEXT,
            email TEXT,
            phone TEXT,
            iban TEXT,
            AddressID INTEGER,
            FOREIGN KEY(AddressID) REFERENCES Address(ID)
        )""")

    db.execute("""
        CREATE TABLE Customer (
            ID INTEGER PRIMARY KEY,
            company TEXT,
            PersonID INTEGER,
            FOREIGN KEY(PersonID) REFERENCES Person(ID)
        )""")
    
    db.execute("""
        CREATE TABLE User (
            ID INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            adminrole INTEGER,
            PersonID INTEGER,
            FOREIGN KEY(PersonID) REFERENCES Person(ID)
        )""")
    
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
        "SELECT ID FROM Address WHERE zip = ? AND street = ? AND snumber = ?",
        ('root', 'root', 'root'))
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
        "SELECT ID FROM Person WHERE email = ? AND phone = ? AND iban = ?",
        ('root', 'root', 'root'))
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

def get_user_by_username(username):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT User.ID, User.username, User.password, User.adminrole, Person.ID, Person.name, Person.firstname, Person.email, Person.phone, Person.iban, Address.country, Address.zip, Address.city, Address.street, Address.snumber
        FROM User
        JOIN Person ON User.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
        WHERE User.username = ?
    """, (username,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        address = Address(
            country=row[10],
            zip=row[11],
            city=row[12],
            street=row[13],
            snumber=row[14]
        )
        person = Person(
            id=row[4],  # Hier das id-Attribut setzen
            name=row[5],
            firstname=row[6],
            email=row[7],
            phone=row[8],
            iban=row[9],
            address=address
        )
        user = User(
            id=row[0],
            person=person,
            username=row[1],
            password=row[2],
            adminrole=row[3]
        )
        return user
    return None

def get_all_users():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT User.ID, User.username, User.password, User.adminrole, Person.ID, Person.name, Person.firstname, Person.email, Person.phone, Person.iban, Address.country, Address.zip, Address.city, Address.street, Address.snumber
        FROM User
        JOIN Person ON User.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
    """)
    rows = cursor.fetchall()
    conn.close()
    
    users = []
    for row in rows:
        address = Address(
            country=row[10],
            zip=row[11],
            city=row[12],
            street=row[13],
            snumber=row[14]
        )
        person = Person(
            id=row[4],  # Hier das id-Attribut setzen
            name=row[5],
            firstname=row[6],
            email=row[7],
            phone=row[8],
            iban=row[9],
            address=address
        )
        user = User(
            id=row[0],
            person=person,
            username=row[1],
            password=row[2],
            adminrole=row[3]
        )
        users.append(user)
    
    return users

def get_user_by_id(user_id):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT User.ID, User.username, User.password, User.adminrole, Person.ID, Person.name, Person.firstname, Person.email, Person.phone, Person.iban, Address.country, Address.zip, Address.city, Address.street, Address.snumber
        FROM User
        JOIN Person ON User.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
        WHERE User.ID = ?
    """, (user_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        address = Address(
            country=row[10],
            zip=row[11],
            city=row[12],
            street=row[13],
            snumber=row[14]
        )
        person = Person(
            id=row[4],  # Hier das id-Attribut setzen
            name=row[5],
            firstname=row[6],
            email=row[7],
            phone=row[8],
            iban=row[9],
            address=address
        )
        user = User(
            id=row[0],
            person=person,
            username=row[1],
            password=row[2],
            adminrole=row[3]
        )
        return user
    return None

def update_user_in_db(user):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    # Update Address
    cursor.execute("""
        UPDATE Address
        SET country = ?, zip = ?, city = ?, street = ?, snumber = ?
        WHERE ID = (SELECT AddressID FROM Person WHERE ID = ?)
    """, (user.person.address.country, user.person.address.zip, user.person.address.city, user.person.address.street, user.person.address.snumber, user.person.id))
    
    # Update Person
    cursor.execute("""
        UPDATE Person
        SET name = ?, firstname = ?, email = ?, phone = ?, iban = ?
        WHERE ID = ?
    """, (user.person.name, user.person.firstname, user.person.email, user.person.phone, user.person.iban, user.person.id))
    
    # Update User
    cursor.execute("""
        UPDATE User
        SET username = ?, password = ?, adminrole = ?
        WHERE ID = ?
    """, (user.username, user.password, user.adminrole, user.id))
    
    conn.commit()
    conn.close()

def delete_user_by_id(user_id):
    db = sqlite3.connect('user.db')
    cur = db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    
    try:
        if user_id:
            cur.execute("SELECT PersonID FROM User WHERE ID = ?", (user_id,))
            person_id = cur.fetchone()
            if person_id:
                person_id = person_id[0]
                cur.execute("SELECT AddressID FROM Person WHERE ID = ?", (person_id,))
                address_id = cur.fetchone()
                if address_id:
                    address_id = address_id[0]
                    cur.execute("DELETE FROM User WHERE ID = ?", (user_id,))
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Customer WHERE PersonID = ?", (person_id,))
                    pid_count = cur.fetchone()[0]
                    cur.execute("SELECT COUNT(*) FROM User WHERE PersonID = ?", (person_id,))
                    uid_count = cur.fetchone()[0]
                    if pid_count == 0 and uid_count == 0:
                        cur.execute("DELETE FROM Person WHERE ID = ?", (person_id,))
                        print(f"{person_id} deleted from Person.")
                    else:
                        print("Cannot delete from Person because it is referenced in other table.")
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Person WHERE AddressID = ?", (address_id,))
                    aid_count = cur.fetchone()[0]
                    if aid_count == 0:
                        cur.execute("DELETE FROM Address WHERE ID = ?", (address_id,))
                        print(f"{address_id} deleted from Address.")
                    else:
                        print("Cannot delete from Address because it is referenced in Person.")
                    db.commit()
                else:
                    print(f"No address found with the provided data for {address_id}.")
            else:
                print(f"No person found with the provided data for {person_id}.")
        else:
            print(f"No user found with the provided data for {user_id}.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

def searchUserDB(search):
    db = sqlite3.connect('user.db')
    cur = db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute(
        """SELECT User.ID, User.username, User.password, User.adminrole, 
                  Person.name, Person.firstname, Person.email, Person.phone, Person.iban, 
                  Address.country, Address.zip, Address.city, Address.street, Address.snumber 
        FROM User 
        JOIN Person ON User.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
        WHERE User.ID LIKE ? OR 
        User.username LIKE ? OR 
        User.PersonID LIKE ? OR
        Person.name LIKE ? OR
        Person.firstname LIKE ? OR
        Person.email LIKE ? OR
        Person.phone LIKE ? OR
        Person.iban LIKE ? OR
        Address.country LIKE ? OR
        Address.zip LIKE ? OR
        Address.city LIKE ? OR
        Address.street LIKE ? OR
        Address.snumber LIKE ?;
        """, (f'%{search}%',)*13)
    results = cur.fetchall()
    db.close()

    users = []
    for row in results:
        address = Address(row[9], row[10], row[11], row[12], row[13])
        person = Person(row[4], row[5], row[6], row[7], row[8], address)
        user = User(row[0], person, row[1], row[2], row[3])
        users.append(user)
    return users

def get_customers():
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    cursor.execute("""
        SELECT c.ID, c.company, p.firstname, p.name, p.email, p.phone, p.iban, a.country, a.zip, a.city, a.street, a.snumber, p.ID
        FROM Customer c
        JOIN Person p ON c.PersonID = p.ID
        JOIN Address a ON p.AddressID = a.ID
    """)
    customers = []
    for row in cursor.fetchall():
        address = Address(row[7], row[8], row[9], row[10], row[11])
        person = Person(row[2], row[3], row[4], row[5], row[6], address, row[12])
        customer = Customer(person, row[1])
        customers.append(customer)
    db.close()
    return customers

def get_current_user():
    user_id = session.get('user_id')
    if user_id:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        cursor.execute("SELECT username FROM User WHERE ID = ?", (user_id,))
        user = cursor.fetchone()
        db.close()
        if user:
            return {'username': user[0]}
    return None

def get_customers_from_db(search_query=None):
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    
    if search_query:
        cursor.execute("""
            SELECT c.ID, c.company, p.name, p.firstname, p.email, p.phone, p.iban, a.country, a.zip, a.city, a.street, a.snumber, p.ID
            FROM Customer c
            JOIN Person p ON c.PersonID = p.ID
            JOIN Address a ON p.AddressID = a.ID
            WHERE p.name LIKE ? OR p.firstname LIKE ? OR p.email LIKE ? OR p.phone LIKE ? OR c.company LIKE ?
        """, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute("""
            SELECT c.ID, c.company, p.name, p.firstname, p.email, p.phone, p.iban, a.country, a.zip, a.city, a.street, a.snumber, p.ID
            FROM Customer c
            JOIN Person p ON c.PersonID = p.ID
            JOIN Address a ON p.AddressID = a.ID
        """)
    
    customers = []
    for row in cursor.fetchall():
        address = Address(row[7], row[8], row[9], row[10], row[11])
        person = Person(row[2], row[3], row[4], row[5], row[6], address, row[12])
        customer = Customer(person, row[1])
        customers.append(customer)
    
    db.close()
    return customers