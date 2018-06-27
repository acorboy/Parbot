from addressGenerator import generate_address
from nameGenerator import generate_company, generate_person

import random

print("Address")
print("*******")

countryindex = random.randint(0, 2)

for _ in range(10):
    t = generate_address(countryindex)
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
    print("vendor name>> ", t.vendor_name)
    print("-------------")

print("Person")
print("*******")

for _ in range(10):
    t = generate_person(countryindex)
    print("fullname>>       ", t.fullname)
    print("first name>>     ", t.first_name)
    print("last name>>      ", t.last_name)
    print("suffix>>         ", t.suffix)
    print("job title>>      ", t.job_title)
    print("telephone>>      ", t.telephone)
    print("fax number>>     ", t.fax_number)
    print("contact number>> ", t.contact_phone)
    print("-------------")