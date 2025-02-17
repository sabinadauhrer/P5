#import random
#import string
#from flask_mail import Message
#from app import mail
#
#def generate_2fa_code(length=6):
#    return ''.join(random.choices(string.digits, k=length))
##
#def send_2fa_code(email, code):
#    msg = Message('Your 2FA Code', sender='your-email@example.com', recipients=[email])
#    msg.body = f'Your 2FA code is: {code}'
#    mail.send(msg)