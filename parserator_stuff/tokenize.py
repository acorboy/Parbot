import os
import

LABELS = ["buyer_name",
          "vendor_name",
          "vendor_legal_name",
          "vendor_id", "tax_id",
          "vendor_site_id",
          "npi",
          "address",
          "address2",
          "city",
          "state",
          "zip",
          "country",
          "phone_number",
          "vendor_contact_name",
          "vendor_contact_title",
          "vendor_contact_phone",
          "vendor_contact_email"]

def tokenize_line(line):
    delimiters = {",": 0, ";": 0, ":": 0, "|": 0, "^": 0, "\t": 0}
    for i in raw_string:
        if i in delimiters.keys():
            delimiters[i] += 1
    number_of_labels = len(LABELS)
    for key in delimiters:
        delimiters[key] = abs(delimiters[key] - number_of_labels)

    delimiter = min(delimiters, key=delimiters.get)

    re_tokens = re.compile("(.+?)(?:{}+|$)".format(delimiter), re.VERBOSE | re.UNICODE)
    tokens = re_tokens.findall(raw_string)
    return tokens
def tokenize_file(file):
    lines= file.split("\n")
    tokenized_lines = []
    for line in lines:
        tokens = tokenize_line(line)
        tokenized_lines.append(tokens)
    return tokenized_lines
