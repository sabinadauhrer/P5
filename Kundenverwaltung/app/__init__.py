from flask import Flask
from app.controllers.user_controller import user_bp
#from flask_mail import Mail, Message



def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'user.db'
    app.register_blueprint(user_bp)

#    app.config['MAIL_SERVER'] = 'smtp.example.com'
#    app.config['MAIL_PORT'] = 587
#    app.config['MAIL_USE_TLS'] = True
#    app.config['MAIL_USERNAME'] = 'your-email@example.com'
#    app.config['MAIL_PASSWORD'] = 'your-email-password'

#    mail = Mail(app)


    return app