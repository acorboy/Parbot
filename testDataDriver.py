from supplier_contactGenerator import generate_supplier, generate_company, generate_contact

import random

countryindex = random.randint(0, 2)

print("Supplier")
print("*******")

for _ in range(10):
    t = generate_supplier()

    print("supplier name>>       ", t.supplier_name)
    print("supplier legal name>> ", t.supplier_legal_name)
    print("tax ID>>              ", t.tax_id)
    print("supplier ID>>         ", t.supplier_id)
    print("supplier site ID>>    ", t.supplier_site_id)
    print("-------------")


print("Address")
print("*******")

for _ in range(10):
    t = generate_company(countryindex)

    print("address line 1>> ", t.address_line1)
    print("address line 2>> ", t.address_line2)
    print("city>>           ", t.city)
    print("state/province>> ", t.state)
    print("postal code>>    ", t.postalCode)
    print("country>>        ", t.country)
    print("-------------")


print("Company")
print("*******")

for _ in range(10):
    t = generate_company()

    print("company phone #>>     ", t.telephone)
    print("company fax phone #>> ", t.fax_number)
    print("-------------")

print("Contact")
print("*******")

for _ in range(10):
    t = generate_contact(countryindex)

    print("first name>>     ", t.first_name)
    print("last name>>      ", t.last_name)
    print("suffix>>         ", t.suffix)
    print("fullname>>       ", t.fullname)
    print("job title>>      ", t.job_title)
    print("contact number>> ", t.contact_phone)
    print("contact email>>  ", t.email)
    print("-------------")
