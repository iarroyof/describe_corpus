import sys
import csv
import codecs
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(binary = True, decode_error = u'ignore', encoding='latin-1', lowercase=True)
word_tokenizer = vectorizer.build_tokenizer()

with codecs.open(sys.argv[1], encoding="latin-1") as cf, codecs.open(sys.argv[2], "w", encoding="latin-1") as of:
    CSV = csv.reader(cf, delimiter=',')
    for i in CSV: 
        try:
            string = word_tokenizer(i[1])
        except:
            continue

        of.write("%s\n" % " ".join(string).lower())
