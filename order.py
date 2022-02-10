class CreditCard:
    valid_month: int
    valid_year: int
    credit_card_owner: str
    credit_card_number: str
    cvv: int

    def __init__(self, valid_month, valid_year, credit_card_owner, credit_card_number, cvv):
        self.valid_month = valid_month
        self.valid_year = valid_year
        self.credit_card_owner = credit_card_owner
        self.credit_card_number = credit_card_number
        self.cvv = cvv


class Address:
    firstname: str
    lastname: str
    street: str
    house_number: int
    zip_code: int
    city: str

    def __init__(self, firstname, lastname, street, house_number, zip_code, city):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city


class Order:
    address: Address
    credit_card: CreditCard
    card: dict[int, int]

    def __init__(self, address, credit_card, card):
        self.address = address
        self.credit_card = credit_card
        self.card = card
