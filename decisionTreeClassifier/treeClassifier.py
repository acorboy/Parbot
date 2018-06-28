from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn import tree
from sklearn.externals import joblib
import xml.etree.ElementTree as ET
import sys
import os
import graphviz

COUNTRY = ["usa", "united states", "can", "canada"]
KEYWORDS = ["inc", "corp", "llc", "ltd"]


def create_dataset(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    data = []
    for child in root:
        for label in child:
            temp = ""
            if label.tag in ["buyer_name", "vendor_name", "vendor_legal_name", "vendor_contact_name"]:
                temp = "name"
            toop = ""
            if temp:
                toop = (label.text, temp)
            else:
                toop = (label.text, label.tag)
            data.append(toop)
    return data



def get_features(word):
    """
    Get features for a given word
    sentence is a set of tokens
    """
    if not word:
        features = {
            'length': 0,
            'spaces': 0,
            'dashes': 0,
            'ats': 0,
            'is_digit': False,
            'is_capitalized': False,
            'is_all_caps': False,
            'is_all_lower': False,
            'capitals_inside': False,
            'is_corp': False,
            'num_non_alphanum': False

        }
        return features

    features = {
            'length': len(word),
            'spaces': word.count(' '),
            'dashes': word.count('-'),
            'ats': word.count('@'),
            'is_digit': word.isdigit(),
            'is_capitalized': word[0].isupper(),
            'is_all_caps': word.isupper(),
            'is_all_lower': word.islower(),
            'capitals_inside': word[1:].isupper(),
            'is_corp': get_is_corp(word),
            'num_non_alphanum': get_nonalphanum_num(word)


    }
    return features


def get_nonalphanum_num(word):
    return sum(not w.isalnum() for w in word)


def get_is_corp(word):
    ending = word.split(" ")[-1].lower()
    if ending in KEYWORDS:
        return True
    return False


def get_is_country(word):
    if word in COUNTRY:
        return True


def untag(tagged_pair):
    """this should be a tuple"""
    return tagged_pair[0]


folder_name = sys.argv[1]

def get_test_files(folder):
    """ Filter out xml files from test data folder, take only those."""
    files = os.listdir(path=folder)
    temp = []
    for file in files:
        ext = file.split(".")[-1]
        if ext == "xml":
            temp.append(file)
    return temp


def open_and_read_files(folder, file_names):
    data = []
    for file in file_names:
        temp = create_dataset(os.path.join(folder, file))
        data += temp
    return data


# this is good here
files = get_test_files(folder_name)
tagged_pairs = open_and_read_files(folder_name, files)

# Split the dataset for training and testing
cutoff = int(.75 * len(tagged_pairs))
training_pairs = tagged_pairs[:cutoff]
test_pairs = tagged_pairs[cutoff:]
 
def transform_to_dataset(tagged_pairs):
    X, Y = [], []
 
    for tagged in tagged_pairs:
        X.append(get_features(untag(tagged)))
        Y.append(tagged[1])
 
    return X, Y
 
X, Y = transform_to_dataset(training_pairs)

clf = Pipeline([
        ('vectorizer', DictVectorizer(sparse=False)),
        ('classifier', DecisionTreeClassifier(criterion='entropy'))
    ])

clf = clf.fit(X[:], Y[:])
joblib.dump(clf, 'model.pkl')


# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")

X_test, Y_test = transform_to_dataset(test_pairs)

print(clf.score(X_test, Y_test))
print(clf.predict(get_features("United States of America")))
