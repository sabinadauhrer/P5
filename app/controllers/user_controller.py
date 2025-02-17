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
    return render_template('user_dashboard.html')

@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))