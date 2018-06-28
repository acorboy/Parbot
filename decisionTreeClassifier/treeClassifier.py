from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
import xml.etree.ElementTree as ET
import sys


def create_dataset(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    data = []
    for child in root:
        for label in child:
            temp = (label.text, label.tag)
            data.append(temp)
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
            'capitals_inside': False

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
            'capitals_inside': word[1:].isupper()

    }
    return features

def untag(tagged_pair):
    """this should be a tuple"""
    return tagged_pair[0]


file_name = sys.argv[1]
# this is good here
tagged_pairs = create_dataset(file_name)

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

clf.fit(X[:], Y[:])

X_test, Y_test = transform_to_dataset(test_pairs)

print(clf.score(X_test, Y_test))