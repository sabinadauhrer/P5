
import sqlite3

def updateDB():
    db=sqlite3.connect('user.db')
    
    db.commit()
    db.close()
