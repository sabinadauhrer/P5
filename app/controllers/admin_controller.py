from flask import Blueprint, request, session, render_template, request, redirect, url_for
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
        return redirect(url_for('user.login'))
    users = get_all_users()
    return render_template('admin_dashboard.html', users=users)

@admin_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if not session.get('is_admin'):
        return redirect(url_for('user.login'))
    
    if request.method == 'POST':
        data = request.form
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
            adminrole=1 if 'is_admin' in data else 0
        )
        new_user_id = save_user_to_db(user)

        # Nach erfolgreicher Registrierung zum Admin-Dashboard weiterleiten
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('admin_add_user.html')

@admin_bp.route('/config')
def config_form():
    config_values = {
        'two_fa_on': config.two_fa_on,
        'session_lifetime': config.session_lifetime,
        'mail_server': config.mail_server,
        'mail_port': config.mail_port,
        'mail_use_tls': config.mail_use_tls,
        'mail_username': config.mail_username,
        'mail_password': config.mail_password
    }
    return render_template('admin_settings.html', config=config_values)

@admin_bp.route('/update_config', methods=['POST'])
def update_config():
    config.two_fa_on = 'two_fa_on' in request.form
    config.session_lifetime = int(request.form['session_lifetime'])
    config.mail_server = request.form['mail_server']
    config.mail_port = int(request.form['mail_port'])
    config.mail_use_tls = 'mail_use_tls' in request.form
    config.mail_username = request.form['mail_username']
    config.mail_password = request.form['mail_password']
    
    # Schreibe die Änderungen in die config.py-Datei
    with open('config.py', 'w') as f:
        f.write(f"two_fa_on = {config.two_fa_on}\n")
        f.write(f"session_lifetime = {config.session_lifetime}\n")
        f.write(f"mail_server = '{config.mail_server}'\n")
        f.write(f"mail_port = {config.mail_port}\n")
        f.write(f"mail_use_tls = {config.mail_use_tls}\n")
        f.write(f"mail_username = '{config.mail_username}'\n")
        f.write(f"mail_password = '{config.mail_password}'\n")
    
    return "Config updated successfully!"