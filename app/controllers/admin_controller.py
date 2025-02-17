from flask import Blueprint, request, jsonify, session, render_template, request, redirect, url_for
from app.models.user import User
from app.models.person import Person
from app.models.address import Address
from app.database.database import *
from app.models.hash import hash_password, verify_password
#from app.utils.auth_utils import generate_2fa_code, send_2fa_code

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('is_admin'):
        return redirect(url_for('login'))
    users = get_all_users()
    return render_template('admin_dashboard.html', users=users)

@admin_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    address = Address(
        country=data['country'],
        zip=data['zip'],
        city=data['city'],
        street=data['street'],
        snumber=data['snumber']
    )
    person = Person(
        name=data['name'],
        firstname=data['firstname'],
        email=data['email'],
        phone=data['phone'],
        iban=data['iban'],
        address=address
    )
    hashed_password = hash_password(data['password'])
    user = User(
        id=None,
        person=person,
        username=data['username'],
        password=hashed_password,
        adminrole=data.get('adminrole', 0)
    )
    new_user_id = save_user_to_db(user)

    return jsonify({"message": "Neuer Benutzer angelegt", "user_id": new_user_id})