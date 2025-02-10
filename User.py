import Address
Address=Address.Address

class User:
    def __init__(self, username, name, firstname, email, iban, Address):
        self.username=username
        self.name=name
        self.firstname=firstname
        self.email=email
        self.iban=iban
        self.Address=Address
        