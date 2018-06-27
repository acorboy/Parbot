from faker import Faker
import random


def generate_company():
    this_company = Faker()

    class Company:
        def __init__(self):
            self.vendor_name = this_company.company()

    return Company()


def generate_person(country=0):
    if country == 1:
        address_country = "en_US"
    elif country == 2:
        address_country = "en_CA"
    else:
        if bool(random.getrandbits(1)):
            address_country = "en_US"
        else:
            address_country = "en_CA"

    this_person = Faker(address_country)

    class Person:
        def __init__(self):
            self.first_name = this_person.first_name()
            self.last_name = this_person.last_name()
            self.suffix = this_person.suffix()
            self.fullname = this_person.name()
            self.job_title = this_person.job()
            self.email = this_person.email()
            # can return number with extension - do we need a different solution?
            self.telephone = this_person.phone_number()
            self.fax_number = this_person.phone_number()
            self.contact_phone = this_person.phone_number()

    return Person()
