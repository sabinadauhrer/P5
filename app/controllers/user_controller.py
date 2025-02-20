from flask import Blueprint, request, jsonify, session, render_template, request, redirect, url_for
from app.models.user import User
from app.models.person import Person
from app.models.address import Address
from app.database.database import *
from app.models.hash import hash_password, verify_password
#from app.utils.auth_utils import generate_2fa_code, send_2fa_code

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    return redirect(url_for('user.login'))

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user_by_username(username)
        
        if user and verify_password(user.password, password):
            session['user_id'] = user.id
            session['is_admin'] = user.adminrole
            if user.adminrole:
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return redirect(url_for('user.user_dashboard'))
        else:
            return render_template('login.html', error="Ungültiger Benutzername oder Passwort")
    return render_template('login.html')
    
@user_bp.route('/verify_2fa', methods=['POST'])
def verify_2fa():
    data = request.json
    code = data['code']
    
    if code == session.get('2fa_code'):
        user_id = session.get('user_id')
        session.pop('2fa_code', None)
        session.pop('user_id', None)
        return jsonify({"message": "Login erfolgreich", "user_id": user_id}), 200
    else:
        return jsonify({"message": "Ungültiger 2FA-Code"}), 401
    
@user_bp.route('/user_dashboard')
def user_dashboard():
    if session.get('is_admin'):
        return redirect(url_for('admin_dashboard'))
    
    user = get_current_user()  # Funktion zum Abrufen des aktuellen Benutzers
    customers = get_customers()  # Kunden aus der Datenbank abrufen
    return render_template('user_dashboard.html', user=user, customers=customers)

@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))

@user_bp.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        # Personendaten
        name = request.form['name']
        firstname = request.form['firstname']
        email = request.form['email']
        phone = request.form['phone']
        iban = request.form['iban']
        
        # Firmendaten
        company = request.form['company']
        
        # Adressdaten
        country = request.form['country']
        zip_code = request.form['zip']
        city = request.form['city']
        street = request.form['street']
        snumber = request.form['snumber']
        
        # Logik zum Hinzufügen des neuen Kunden in die Datenbank
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        
        # Adresse speichern
        cursor.execute("INSERT INTO Address (country, zip, city, street, snumber) VALUES (?, ?, ?, ?, ?)",
                       (country, zip_code, city, street, snumber))
        address_id = cursor.lastrowid
        
        # Person speichern
        cursor.execute("INSERT INTO Person (name, firstname, email, phone, iban, AddressID) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, firstname, email, phone, iban, address_id))
        person_id = cursor.lastrowid
        
        # Kunde speichern
        cursor.execute("INSERT INTO Customer (company, PersonID) VALUES (?, ?)", (company, person_id))
        
        db.commit()
        db.close()
        
        return redirect(url_for('user.user_dashboard'))
    
    return render_template('user_add_customer.html')

@user_bp.route('/edit_customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    
    if request.method == 'POST':
        # Aktualisierte Daten aus dem Formular abrufen
        name = request.form['name']
        firstname = request.form['firstname']
        email = request.form['email']
        phone = request.form['phone']
        iban = request.form['iban']
        company = request.form['company']
        country = request.form['country']
        zip_code = request.form['zip']
        city = request.form['city']
        street = request.form['street']
        snumber = request.form['snumber']
        
        # Person und Adresse aktualisieren
        cursor.execute("""
            UPDATE Person
            SET name = ?, firstname = ?, email = ?, phone = ?, iban = ?
            WHERE ID = ?
        """, (name, firstname, email, phone, iban, customer_id))
        
        cursor.execute("""
            UPDATE Address
            SET country = ?, zip = ?, city = ?, street = ?, snumber = ?
            WHERE ID = (SELECT AddressID FROM Person WHERE ID = ?)
        """, (country, zip_code, city, street, snumber, customer_id))
        
        # Firma aktualisieren
        cursor.execute("""
            UPDATE Customer
            SET company = ?
            WHERE PersonID = ?
        """, (company, customer_id))
        
        db.commit()
        db.close()
        
        return redirect(url_for('user.user_dashboard'))
    
    # Kundendaten abrufen
    cursor.execute("""
        SELECT p.name, p.firstname, p.email, p.phone, p.iban, c.company, a.country, a.zip, a.city, a.street, a.snumber
        FROM Customer c
        JOIN Person p ON c.PersonID = p.ID
        JOIN Address a ON p.AddressID = a.ID
        WHERE p.ID = ?
    """, (customer_id,))
    customer = cursor.fetchone()
    db.close()
    
    return render_template('user_edit_customer.html', customer=customer, customer_id=customer_id)

@user_bp.route('/delete_customer/<int:customer_id>', methods=['GET', 'POST'])
def delete_customer(customer_id):
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    
    # Adresse-ID abrufen
    cursor.execute("SELECT AddressID FROM Person WHERE ID = ?", (customer_id,))
    address_id = cursor.fetchone()[0]
    
    # Kunde, Person und Adresse löschen
    cursor.execute("DELETE FROM Customer WHERE PersonID = ?", (customer_id,))
    cursor.execute("DELETE FROM Person WHERE ID = ?", (customer_id,))
    cursor.execute("DELETE FROM Address WHERE ID = ?", (address_id,))
    
    db.commit()
    db.close()
    
    return redirect(url_for('user.user_dashboard'))

@user_bp.route('/search_customer', methods=['POST'])
def search_customer():
    search_query = request.form['search']
    customers = get_customers_from_db(search_query)  # Kunden aus der Datenbank abrufen
    user = get_current_user()  # Funktion zum Abrufen des aktuellen Benutzers
    return render_template('user_dashboard.html', user=user, customers=customers)