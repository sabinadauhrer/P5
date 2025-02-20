from flask import Flask, session, redirect, request, url_for
import os
from datetime import timedelta
from app.controllers.user_controller import user_bp
from app.controllers.admin_controller import admin_bp
from app.database.database import *
import config
from flask_mail import Mail, Message


def create_app():
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(__file__), 'views', 'templates'),
                static_folder='views/static')
    
    app.secret_key = os.urandom(24)
    app.config['DATABASE'] = 'user.db'
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=config.session_lifetime)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    
    if config.two_fa_on == True:
        app.config['MAIL_SERVER'] = config.mail_server
        app.config['MAIL_PORT'] = config.mail_port
        app.config['MAIL_USE_TLS'] = config.mail_use_tls
        app.config['MAIL_USERNAME'] = config.mail_username
        app.config['MAIL_PASSWORD'] = config.mail_password
        mail = Mail(app)
    else:
        pass

    @app.before_request
    def check_authentication_and_authorization():
        if request.endpoint and 'static' in request.endpoint:
            return  # Erlaubt den Zugriff auf statische Dateien ohne Authentifizierung
        if 'user_id' not in session and request.endpoint not in ['user.login', 'user.index']:
            return redirect(url_for('user.login'))
        if request.endpoint and request.endpoint.startswith('admin.') and not session.get('is_admin'):
            return redirect(url_for('user.login'))

    return app