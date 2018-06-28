from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/Users/temp_account/Downloads/stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz','/Users/temp_account/Downloads/stanford-ner-2018-02-27/stanford-ner.jar', encoding='utf-8')

def parse_data(str_data):
    tokenized_text = word_tokenize(str_data)
    classified_text = st.tag(tokenized_text)
    return classified_text
