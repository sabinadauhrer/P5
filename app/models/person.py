import app.models.address as Address
Address = Address.Address

class Person:
    def __init__(self, name, firstname, email, phone, iban, address, id=None):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.email = email
        self.phone = phone
        self.iban = iban
        self.address = address