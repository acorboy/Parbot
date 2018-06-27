#!/usr/bin/python3

#Parbot Test File Generator

import sys
import random
from datetime import date
from gen_contact_name import gen_contact_name

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
    training_record = ''
    for key in record:
        training_record += record[key] + ','
    training_file.write(training_record + '\n')

# Stub - Function for writing to test file
def write_test(record):
    test_record = ''

# For each file set requested, loop through opening new files, creating records, then closing the files
for i in range(num_file_sets):
    print('file:', i+1)

    # Open a file each iteration of the file loop for each requirement
    base_file_name = 'parbot_' + todays_date + '_file'+ str(i)

    # 1. Open a training file - CSV to start, update to the XML preferred for parserator
    training_file = open(base_file_name+'training.csv', "w")

    # 2. Open a different delimiter file
    #     Choose 1 delimiter randomly from a list of them

    # 3. Open a Variable delimiter file
    #     When writing to this file, randomly choose a delimiter for each line

    # 4. No Delimiter
    #    When writingto this file, concat all without spaces
    #    Note this is not fixed width

    # Add a header record, assign the keys to the values
    column_names = record.keys()
    for i in column_names:
        record[i] = i
    # Always add header to the training file
    write_training(record)

    # Random chance we'll write header to the test file
    #header_chance = random.random()
    #if header_chance > 0.8:

    # Create a new record to be appended to the files.  It will be cleared after its appended.
    for q in range(num_records):
        record['buyer_name'] = 'default'
        record['vendor_name'] = 'default'
        record['vendor_legal_name'] = 'default'
        record['vendor_id'] = 'default'
        record['tax_id'] = 'default'
        record['vendor_site_id'] = 'default'
        record['npi'] = 'default'
        record['address'] = 'default'
        record['address2'] = 'default'
        record['city'] = 'default'
        record['state'] = 'default'
        record['zip'] = 'default'
        record['country'] = 'default'
        record['phone_number'] = 'default'
        record['vendor_contact_name'] = gen_contact_name()
        record['vendor_contact_title'] = 'default'
        record['vendor_contact_phone'] = 'default'
        record['vendor_contact_email'] = 'default'

        print(q)
        # Append record to each open file
        write_training(record)

        # End of Record loop


    # File loop has finished.
    # Log file names

    # Close all open files
    training_file.close()
print('Outside of Loop')