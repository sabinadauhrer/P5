import Address
Address=Address.Address

class Person:
    def __init__(self, name, firstname, email, phone, iban, Address=Address):
        self.name=name
        self.firstname=firstname
        self.email=email
        self.phone=phone
        self.iban=iban
        self.Address=Address
        