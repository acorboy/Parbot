from faker import Faker
import random


def generate_supplier():
    this_supplier = Faker()

    class Supplier:
        def __init__(self):
            self.supplier_name = this_supplier.company()
            if bool(random.getrandbits(1)):
                self.supplier_legal_name = self.supplier_name
            else:
                self.supplier_legal_name = this_supplier.company()
            self.tax_id = str(random.randrange(10, 99)) + "-" + str(random.randrange(1111111, 9999999))

    return Supplier()


def generate_company(country=0):
    if country == 1:
        address_country = "en_US"
    elif country == 2:
        address_country = "en_CA"
    else:
        if bool(random.getrandbits(1)):
            address_country = "en_US"
        else:
            address_country = "en_CA"

    this_company = Faker(address_country)

    class Company:
        def __init__(self):
            # can return number with extension - do we need a different solution?
            self.telephone = this_company.phone_number()
            self.fax_number = this_company.phone_number()

    return Company()


def generate_contact(country=0):
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

    class Contact:
        def __init__(self):
            self.first_name = this_person.first_name()
            self.last_name = this_person.last_name()
            self.suffix = this_person.suffix()

            self.fullname = this_person.name()
            self.job_title = this_person.job()
            self.email = this_person.email()
            self.contact_phone = this_person.phone_number()

    return Contact()
