import random
from time import time
from decimal import Decimal
from faker import Faker

def generate_invoice(country=0):

    if country == 1:
        address_country = "en_US"
    elif country == 2:
        address_country = "en_CA"
    else:
        if bool(random.getrandbits(1)):
            address_country = "en_US"
        else:
            address_country = "en_CA"

    fake_inv = Faker(address_country)

    class Invoice:
        def __init__(self):
            self.Invoice_Count =  fake_inv.random_int()
            self.Invoice_Amount = float(Decimal(random.randrange(500, 10000))/100)
            self.Payment_Count = fake_inv.random_int()
            self.Payment_Amount = float(Decimal(random.randrange(500, 10000))/100)
            if address_country == "en_CA":
                self.Payment_Currency = fake_inv.random_element(elements=("Canada", "CA", "Cad", "CAN", "CAD"))
            else:
                self.Payment_Currency = fake_inv.random_element(elements=("USD", "US", "USA"))
    return Invoice()


