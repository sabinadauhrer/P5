from flask import Flask
import os
from app.controllers.user_controller import user_bp
from app.controllers.admin_controller import admin_bp
from app.database.database import *
#from flask_mail import Mail, Message



def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'views', 'templates'))
    app.secret_key = 'your_secret_key'
    app.config['DATABASE'] = 'user.db'
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

#    app.config['MAIL_SERVER'] = 'smtp.example.com'
#    app.config['MAIL_PORT'] = 587
#    app.config['MAIL_USE_TLS'] = True
#    app.config['MAIL_USERNAME'] = 'your-email@example.com'
#    app.config['MAIL_PASSWORD'] = 'your-email-password'

#    mail = Mail(app)


    return app