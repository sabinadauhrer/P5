from flask import Blueprint, request, jsonify, session
from app.models.user import User
from app.models.person import Person
from app.models.address import Address
from app.database.database import *
from app.models.hash import hash_password, verify_password
#from app.utils.auth_utils import generate_2fa_code, send_2fa_code

user_bp = Blueprint('user', __name__)

@user_bp.route('/add_user', methods=['POST'])
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

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    
    user = get_user_by_username(username)
    
    if user and verify_password(user.password, password):
        return jsonify({"message": "Login erfolgreich", "user_id": user.id})
    else:
        return jsonify({"message": "Ungültiger Benutzername oder Passwort"}), 401
    
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