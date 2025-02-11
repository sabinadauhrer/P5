
import csv
import sqlite3

def seedDB():
    db=sqlite3.connect('user.db')
    
    db.commit()
    db.close()
    