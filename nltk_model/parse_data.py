from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/Users/temp_account/Downloads/stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz','/Users/temp_account/Downloads/stanford-ner-2018-02-27/stanford-ner.jar', encoding='utf-8')

text = "Perez-Turner Ryan, Simpson and Escobar Bartlett, James and Robinson,423352301c8142bc13ea4344115013b5,15-7380349,27.523780:83.345585,8288140737,68297 Scott Orchard,South Derrick,NE,31056,United States of America,203-220-8928,Susan Bender,Engineer, biomedical,1-552-632-8506,evanscody@oneill.info"

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

for i in classified_text:
    print(i)
