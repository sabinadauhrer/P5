
import Address
import Person
import Customer
import User
#import Admin

Address=Address.Address
Person=Person.Person
Customer=Customer.Customer
User=User.User
#Admin=Admin.Admin

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
            , username TEXT UNIQUE
            , password TEXT
            , adminrole INTEGER
            , PersonID INTEGER
            , PRIMARY KEY(ID), FOREIGN KEY(PersonID) REFERENCES Person(ID))""")

    db.commit()
    db.close()
    seedroot()
# --- seed root ---
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
# --- seed ---
def seedAddress(Address):
    data=[Address.getCountry(),Address.getZIP(),Address.getCity(),Address.getStreet(),Address.getSnumber()]
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    try:
        cur.execute("""INSERT INTO Address (
            country,
            zip,
            city,
            street,
            snumber
            ) VALUES (?, ?, ?, ?, ?);""", data)
    except sqlite3.Error as e:
        print(f"an error occurred: {e}")
    db.commit()
    db.close()
    
def seedPerson(Person):
    padata=[Person.getZIP(),Person.getStreet(),Person.getSnumber()]
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Address WHERE zip = ? AND street = ? AND snumber = ?"
        , (padata))
    AddressID=cur.fetchone()
    if AddressID:
        AddressID=AddressID[0]
        data=[Person.getName(),Person.getFirstname(),Person.getEmail(),Person.getPhone(),Person.getIBAN(),AddressID]
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
    
def seedUser(User):
    updata=[User.getEmail(),User.getPhone(),User.getIBAN()]
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Person WHERE email = ? AND phone = ? AND iban = ?"
        , (updata))
    PersonID=cur.fetchone()
    if PersonID:
        PersonID=PersonID[0]
        data=[User.getUsername(),User.getPassword(),0,PersonID]
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
    
def seedUserComplete(User,Person,Address):
    seedAddress(Address)
    seedPerson(Person)
    seedUser(User)
    
def seedCustomer(Customer):
    cpdata=[Customer.getEmail(),Customer.getPhone(),Customer.getIBAN()]
    db=sqlite3.connect('user.db')    
    cur=db.cursor()
    cur.execute(
        "SELECT id FROM Person WHERE email = ? AND phone = ? AND iban = ?"
        , (cpdata))
    PersonID=cur.fetchone()
    if PersonID:
        PersonID=PersonID[0]
        data=[Customer.getCompany(),PersonID]
        cur.execute("""INSERT INTO Customer (
            company,
            PersonID
            ) VALUES (?, ?);""", data)
        db.commit()
    else:
        print(f"No address found with the provided data for {Customer.getEmail()}, {Customer.getPhone()}, {Customer.getIBAN()}.")
    db.close()

def seedCustomerComplete(Customer,Person,Address):
    seedAddress(Address)
    seedPerson(Person)
    seedCustomer(Customer)
# --- search ---
def searchUserDB(search):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute(
        f"""SELECT User.*, Person.*, Address.* 
        FROM User 
        JOIN Person ON User.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
        WHERE User.ID LIKE {search} OR 
        User.username LIKE {search} OR 
        User.PersonID LIKE {search} OR
        Person.name LIKE {search} OR
        Person.firstname LIKE {search} OR
        Person.email LIKE {search} OR
        Person.phone LIKE {search} OR
        Person.iban LIKE {search} OR
        Address.country LIKE {search} OR
        Address.zip LIKE {search} OR
        Address.city LIKE {search} OR
        Address.street LIKE {search} OR
        Address.snumber LIKE {search};
        """)
    results=cur.fetchall()
    db.close()
    return results
    
def searchCustomerDB(search):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute(
        f"""SELECT Customer.*, Person.*, Address.* 
        FROM Customer 
        JOIN Person ON Customer.PersonID = Person.ID
        JOIN Address ON Person.AddressID = Address.ID
        WHERE Customer.ID LIKE {search} OR 
        Customer.company LIKE {search} OR 
        Customer.PersonID LIKE {search} OR
        Person.name LIKE {search} OR
        Person.firstname LIKE {search} OR
        Person.email LIKE {search} OR
        Person.phone LIKE {search} OR
        Person.iban LIKE {search} OR
        Address.country LIKE {search} OR
        Address.zip LIKE {search} OR
        Address.city LIKE {search} OR
        Address.street LIKE {search} OR
        Address.snumber LIKE {search};
        """)
    results=cur.fetchall()
    db.close()
    return results
# --- delete ---    
def deleteCustomerN(name,firstname,email,phone,iban):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    
    try:
        cur.execute("SELECT ID FROM Person WHERE name = ? AND firstname = ? AND email = ? AND phone = ? AND iban = ?", (name,firstname,email,phone,iban))
        PersonID=cur.fetchone()
        if PersonID:
            PersonID=PersonID[0]
            cur.execute("SELECT AddressID FROM Person WHERE ID = ?", (PersonID,))
            AddressID=cur.fetchone()        
            if AddressID:
                AddressID=AddressID[0]
                cur.execute("SELECT ID FROM Customer WHERE PersonID = ?", (PersonID,))
                CustomerID=cur.fetchone()        
                if CustomerID:
                    CustomerID=CustomerID[0]
                    cur.execute("DELETE FROM Customer WHERE ID = ?", (CustomerID,))
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Customer WHERE PersonID = ?",(PersonID,))
                    pidcount=cur.fetchone()[0]
                    if pidcount==0:
                        cur.execute("DELETE FROM Person WHERE ID = ?",(PersonID,))
                        print(f"{PersonID} deleted from Person.")
                    else:
                        print("Cannot delete from Person because it is referenced in Customer.")
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Person WHERE AddressID = ?",(AddressID,))
                    aidcount=cur.fetchone()[0]
                    if aidcount==0:
                        cur.execute("DELETE FROM Address WHERE ID = ?",(AddressID,))
                        print(f"{AddressID} deleted from Address.")
                    else:
                        print("Cannot delete from Address because it is referenced in Person.")
                    db.commit()
                    db.close()
                else:
                    print(f"No address found with the provided data for {CustomerID}.")
            else:
                print(f"No address found with the provided data for {AddressID}.")
        else:
            print(f"No address found with the provided data for {PersonID}.")
    except sqlite3.Error as e:
        print(f"an error occurred: {e}")
    db.close()
    
def deleteCustomerID(CustomerID):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    
    try:
        cur.execute("SELECT PersonID FROM Customer WHERE ID = ?", (CustomerID,))
        PersonID=cur.fetchone()
        if PersonID:
            PersonID=PersonID[0]
            cur.execute("SELECT AddressID FROM Person WHERE ID = ?", (PersonID,))
            AddressID=cur.fetchone()        
            if AddressID:
                AddressID=AddressID[0]
                if CustomerID:
                    cur.execute("DELETE FROM Customer WHERE ID = ?", (CustomerID,))
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Customer WHERE PersonID = ?",(PersonID,))
                    pidcount=cur.fetchone()[0]
                    if pidcount==0:
                        cur.execute("DELETE FROM Person WHERE ID = ?",(PersonID,))
                        print(f"{PersonID} deleted from Person.")
                    else:
                        print("Cannot delete from Person because it is referenced in Customer.")
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Person WHERE AddressID = ?",(AddressID,))
                    aidcount=cur.fetchone()[0]
                    if aidcount==0:
                        cur.execute("DELETE FROM Address WHERE ID = ?",(AddressID,))
                        print(f"{AddressID} deleted from Address.")
                    else:
                        print("Cannot delete from Address because it is referenced in Person.")
                    db.commit()
                    db.close()
                else:
                    print(f"No address found with the provided data for {CustomerID}.")
            else:
                print(f"No address found with the provided data for {AddressID}.")
        else:
            print(f"No address found with the provided data for {PersonID}.")
    except sqlite3.Error as e:
        print(f"an error occurred: {e}")
    db.close()

def deleteUserN(username):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    
    try:
        cur.execute("SELECT ID FROM User WHERE username = ?", (username,))
        UserID=cur.fetchone()
        if UserID:
            UserID=UserID[0]
            cur.execute("SELECT PersonID FROM User WHERE ID = ?", (UserID,))
            PersonID=cur.fetchone()        
            if PersonID:
                PersonID=PersonID[0]
                cur.execute("SELECT AddressID FROM Person WHERE ID = ?", (PersonID,))
                AddressID=cur.fetchone()
                if AddressID:
                    AddressID=AddressID[0]
                    cur.execute("DELETE FROM User WHERE ID = ?", (UserID,))
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Customer WHERE PersonID = ?",(PersonID,))
                    pidcount=cur.fetchone()[0]
                    cur.execute("SELECT COUNT(*) FROM User WHERE PersonID = ?",(PersonID,))
                    uidcount=cur.fetchone()[0]
                    if pidcount==0 and uidcount==0:
                        cur.execute("DELETE FROM Person WHERE ID = ?",(PersonID,))
                        print(f"{PersonID} deleted from Person.")
                    else:
                        print("Cannot delete from Person because it is referenced in other table.")
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Person WHERE AddressID = ?",(AddressID,))
                    aidcount=cur.fetchone()[0]
                    if aidcount==0:
                        cur.execute("DELETE FROM Address WHERE ID = ?",(AddressID,))
                        print(f"{AddressID} deleted from Address.")
                    else:
                        print("Cannot delete from Address because it is referenced in Person.")
                    db.commit()
                    db.close()
                else:
                    print(f"No address found with the provided data for {AddressID}.")
            else:
                print(f"No address found with the provided data for {PersonID}.")
        else:
            print(f"No address found with the provided data for {UserID}.")
    except sqlite3.Error as e:
        print(f"an error occurred: {e}")
    db.close()

def deleteUserID(UserID):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    
    try:
        if UserID:
            cur.execute("SELECT PersonID FROM User WHERE ID = ?", (UserID,))
            PersonID=cur.fetchone()        
            if PersonID:
                PersonID=PersonID[0]
                cur.execute("SELECT AddressID FROM Person WHERE ID = ?", (PersonID,))
                AddressID=cur.fetchone()
                if AddressID:
                    AddressID=AddressID[0]
                    cur.execute("DELETE FROM User WHERE ID = ?", (UserID,))
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Customer WHERE PersonID = ?",(PersonID,))
                    pidcount=cur.fetchone()[0]
                    cur.execute("SELECT COUNT(*) FROM User WHERE PersonID = ?",(PersonID,))
                    uidcount=cur.fetchone()[0]
                    if pidcount==0 and uidcount==0:
                        cur.execute("DELETE FROM Person WHERE ID = ?",(PersonID,))
                        print(f"{PersonID} deleted from Person.")
                    else:
                        print("Cannot delete from Person because it is referenced in other table.")
                    db.commit()
                    cur.execute("SELECT COUNT(*) FROM Person WHERE AddressID = ?",(AddressID,))
                    aidcount=cur.fetchone()[0]
                    if aidcount==0:
                        cur.execute("DELETE FROM Address WHERE ID = ?",(AddressID,))
                        print(f"{AddressID} deleted from Address.")
                    else:
                        print("Cannot delete from Address because it is referenced in Person.")
                    db.commit()
                    db.close()
                else:
                    print(f"No address found with the provided data for {AddressID}.")
            else:
                print(f"No address found with the provided data for {PersonID}.")
        else:
            print(f"No address found with the provided data for {UserID}.")
    except sqlite3.Error as e:
        print(f"an error occurred: {e}")
    db.close()
# --- update ---    
def updateUser(column,value,ID):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute(f"""
                UPDATE User
                SET {column} = ?
                WHERE ID = ?;
                """, (value,ID))
    db.commit()
    db.close()

def updateUserPW(value,ID):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""
                UPDATE User
                SET password = ?
                WHERE ID = ?;
                """, (value,ID))
    db.commit()
    db.close()

def updateCustomer(column,value,ID):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute(f"""
                UPDATE Customer
                SET {column} = ?
                WHERE ID = ?;
                """, (value,ID))
    db.commit()
    db.close()

def gettablecolumns(db):
    tables=[]
    db.execute("PRAGMA foreign_keys = ON;")
    for row in db.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        tablename=row[0]
        columns=[]
        for columnrow in db.execute(f"PRAGMA table_info({tablename});"):
            columns.append(columnrow[1])
        tables.append((tablename, columns))
    return tables

def updatevalueincolumn(db, columnname, newvalue, idvalue):
    tables=gettablecolumns(db)
    for tablename, columns in tables:
        if columnname in columns:
            db.execute(f"UPDATE {tablename} SET {columnname} = ? WHERE ID = ?",(newvalue, idvalue))
            db.commit()
            print(f"Updated {columnname} in table {tablename} where ID = {idvalue}")
            return True
    return False

def updateDB(column, value, ID):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    try:
        cur.execute("PRAGMA foreign_keys = ON;")
        if not updatevalueincolumn(cur, column, value, ID):
            print(f"Column '{column}' not found in any table.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()
# --- login ---
def readLoginDB(username, password):
    db=sqlite3.connect('user.db')
    cur=db.cursor()
    
    cur.execute("SELECT PersonID FROM User WHERE username = ? AND password = ?", (username, password))
    PersonID=cur.fetchone()
    
    if PersonID:
        PersonID=PersonID[0]
        cur.execute("SELECT AddressID FROM Person WHERE ID = ?", (PersonID,))
        AddressID=cur.fetchone()        
        adata=None
        if AddressID:
            AddressID=AddressID[0]
            cur.execute("SELECT country, zip, city, street, snumber FROM Address WHERE ID = ?", (AddressID,))
            adata=cur.fetchone()
        cur.execute("SELECT name, firstname, email, phone, iban FROM Person WHERE ID = ?", (PersonID,))
        pdata=cur.fetchone()
        cur.execute("SELECT username, password FROM User WHERE username = ? AND password = ?", (username, password))
        udata=cur.fetchone()
        cur.execute("SELECT adminrole FROM User WHERE username = ? AND password = ?", (username, password))
        admincheck=cur.fetchone()
        
        db.commit()
        db.close()
        
        return {
            'Address': adata,
            'Person': pdata,
            'User': udata,
            'Admin': admincheck[0] if admincheck else None
        }
    else:
        print(f"No user found with the provided data for {username}.")
        db.commit()
        db.close()
        return 
