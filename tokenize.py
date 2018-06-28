import os
import
from sklearn.externals import joblib
from decisionTreeClassifier.treeClassifier import get_features
import os
import pandas as pd
dir_path = os.path.dirname(os.path.realpath(__file__))
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

def classify(tokenized_lines):
    cls = joblib.loads(dir_path + '/decisionTreeClassifier/model.pkl')
    lines_predictions = []
    for line in tokenized_lines:
        line_predictions = {}
        for token in line:
            prediction = cls.predict(get_features(token))
            line_predictions[prediction] = tokens
        lines_predictions.append(line_predictions)
    return lines_predictions



def data_frame_func(lines_predictions):
    result = pd.concat([pd.DataFrame(d) for f in lines_predictions], ignore_index=True)
    return(result.to_html())

    #for line in lines_predictions:
    #    data = pd.DataFame(d=line)

def process_file(file):
    tokenized_lines = tokenize_file(file)
    classified_lines = classify(tokenized_lines)
    data_frame = data_frame_func(classified_lines)
    return data_frame
