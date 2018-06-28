from faker import Faker
import random


def generate_address(country=0):
    if country == 1:
        address_country = "en_US"
    elif country == 2:
        address_country = "en_CA"
    else:
        if bool(random.getrandbits(1)):
            address_country = "en_US"
        else:
            address_country = "en_CA"
            
    this_address = Faker(address_country)

    class Address:
        def __init__(self):
            if bool(random.getrandbits(1)):
                self.address_line1 = str(this_address.random_int()) + " " + this_address.street_name()
                if bool(random.getrandbits(1)):
                    self.address_line2 = this_address.secondary_address()
                else:
                    self.address_line2 = " "
            else:
                self.address_line1 = this_address.street_address()
                self.address_line2 = " "
            self.city = this_address.city()
            if address_country == "en_CA":
                if bool(random.getrandbits(1)):
                    self.state = this_address.province()
                else:
                    self.state = this_address.province_abbr()
            else:
                if bool(random.getrandbits(1)):
                    self.state = this_address.state()
                else:
                    self.state = this_address.state_abbr()
            self.postalCode = this_address.postalcode()
            if address_country == "en_CA":
                self.country = this_address.random_element(elements=("Canada", "CA", "Can"))
            else:
                self.country = this_address.random_element(elements=("USA", "US", "U.S.A", "U.S.",
                                                                     "United States of America"))
    return Address()

