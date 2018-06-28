#!/usr/bin/python3

#Parbot Test File Generator
import sys
import random
from datetime import date
from addressGenerator import generate_address
from supplier_contactGenerator import generate_supplier, generate_company, generate_contact



# Parameters: # of files, average record count
num_file_sets = sys.argv[1]
num_records = sys.argv[2]

# Validate the Parameters
# Replace with try-catch?
if len(sys.argv) != 3:
    print ('Invalid number of arguments:',len(sys.argv) -1, ' Only 2 arguments expected.')
    exit()
elif not num_file_sets.isdigit():
    print ('Invalid Argument:', num_file_sets)
    exit()
elif not num_records.isdigit():
    print ('Invalid Argument:', num_records)
    exit()
# Now that their validated, set params to ints
num_file_sets = int(num_file_sets)
num_records = int(num_records)

# Initialize a new dictionary, record. The dictionary will represent 1 line or record.
# The order, number and column names for this version is fixed.
record = {
    # Buyer Name is the Company name or it could be the division or department within the company
    # Examples: Acme, Acme-Shipping Dept, Acme-CustService
    'buyer_name' : '',
    # Vendor's Name is who they buyer purchased goods or services from
    'vendor_name' : '',
    # Vendor Legal Name is the name registered with the government (Optional, can be blank)
    # Think IBM vs. International Business Machine, Inc.
    'vendor_legal_name' : '',
    # Vendor Id is the Id the buyer assigned (Optional, can be blank)
    'vendor_id' : '',
    # tax_id  is the government merchant tax id
    'tax_id' : '',
    #vendor site id refers to a location code the vendor uses (Optional, can be blank)
    'vendor_site_id' : '',
    #npi is never really used - blanks or empty
    'npi' : '',
    # Address line - fill with street #, direction, street name, type. Optional - Unit/Apt/Suite #
    'address' : '',
    # Address line 2 - Optional, can be blank or have Unit/Apt/Suite #
    'address2' : '',
    # City - real cities paired with states is optional. Pattern not validity needed.
    'city' : '',
    # State - 2 letter, 3 letter, or fully spelled out
    'state' : '',
    # zip code can be 5 digits or 5+4 digits
    'zip' : '',
    # Country is only US or Canada, but can be variations on codes for either
    'country' : '',
    # Phone number - 1-XXX-XXX-XXXX or similar patterns
    'phone_number' : '',
    # Contact name should be filled in and connected to email if possible
    'vendor_contact_name' : '',
    # Title can be a random selection from any array - CEO, CIO, Acct Manager, etc
    'vendor_contact_title' : '',
    # Phone number - 1-XXX-XXX-XXXX or similar patterns
    'vendor_contact_phone' : '',
    # For email, try to use the Contact name above
    'vendor_contact_email' : ''
}
# Today's date in YYYY-MM-DD format
todays_date = str(date.today())

def write_training(record):
    training_record = '<TokenSequence>'
    for key in record:
        training_record += '<' + key + '>' + record[key] + '</' + key + '>'
    training_record += '<TokenSequence>'
    training_file.write(training_record + '\n')

# Stub - Function for writing to test file
def write_test(record, delim):
    test_record = ''
    for key in record:
        test_record += record[key] + delim

    test_file_onedelim.write(test_record + '\n')

# For each file set requested, loop through opening new files, creating records, then closing the files
for i in range(num_file_sets):
    print('file:', i+1)

    # Open a file each iteration of the file loop for each requirement
    base_file_name = '..\data\parbot_' + todays_date + '_file'+ str(i)

    # 1. Open a training file - CSV to start, update to the XML preferred for parserator
    training_file = open(base_file_name+'_training.xml', "w")
    # Header for the xml training file
    training_file.write('<Collection>' + '\n')

    # 2. Open a different delimiter file
    #     Choose 1 delimiter randomly from a list of them
    test_file_onedelim = open(base_file_name + '_onedelim.dat', "w")
    delim = ","

    # 3. Open a Variable delimiter file
    #     When writing to this file, randomly choose a delimiter for each line

    # 4. No Delimiter
    #    When writingto this file, concat all without spaces
    #    Note this is not fixed width

    # Add a header record, assign the keys to the values
    column_names = record.keys()
    for i in column_names:
        record[i] = i

    # Random chance we'll write header to the test file
    #header_chance = random.random()
    #if header_chance > 0.8:

    # Create a new record to be appended to the files.  It will be cleared after its appended.
    for q in range(num_records):
        # Random country index for Faker data
        countryindex = random.randint(0, 2)

        # Buyer info. This is separate from the Supplier
        record['buyer_name'] = generate_supplier().supplier_name

        # Supplier Block
        supplier_block = generate_supplier()
        record['vendor_name'] = supplier_block.supplier_name
        record['vendor_legal_name'] = supplier_block.supplier_legal_name

        record['vendor_id'] = 'A21316513'
        record['tax_id'] = '123-45-6789'
        record['vendor_site_id'] = 'Area 51'
        record['npi'] = ''

        # This block sourced from addressGenerator.py generate_address

        address_block = generate_address(countryindex)

        record['address'] = address_block.address_line1
        record['address2'] = address_block.address_line1
        record['city'] = address_block.city
        record['state'] = address_block.state
        record['zip'] = address_block.postalCode
        record['country'] = address_block.country
        # End addressGenerator.py

        record['phone_number'] = generate_company(countryindex).telephone

        # This block sourcedfrom nameGenerator.py generate_person
        contact_block = generate_contact(countryindex)
        record['vendor_contact_name'] = contact_block.fullname
        record['vendor_contact_title'] = contact_block.job_title
        record['vendor_contact_phone'] = contact_block.contact_phone
        record['vendor_contact_email'] = contact_block.email

        # Append record to each open file
        write_training(record)
        write_test(record,delim)

        # End of Record loop


    # File loop has finished.
    # Log file names

    # Close all open files
    test_file_onedelim.close()

    # Trailer for the xml training file
    training_file.write('<Collection>' + '\n')
    training_file.close()
print('Complete')