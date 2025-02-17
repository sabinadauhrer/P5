from flask import Flask, request, jsonify, send_from_directory
from app.Database import add_user, get_user_by_username  # Importieren Sie die Funktion hier
from app.models.Address import Address
from app.models.Person import Person
from app.models.User import User
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DATABASE'] = 'user.db'
# Erstellen Sie die Tabellen beim Start der Anwendung

@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)