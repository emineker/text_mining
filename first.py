# sudo apt-get install python-pip python-mysqldb

# git clone https://github.com/sloria/TextBlob.git
# cd TextBlob
# python setup.py install

# pip install -U textblob
# python -m textblob.download_corpora

from textblob.classifiers import BaseClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob.classifiers import MaxEntClassifier
from textblob.classifiers import NaiveBayesClassifier
from textblob.blob import TextBlob

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

# cl = BaseClassifier(train)
cl = DecisionTreeClassifier(train)
cl = MaxEntClassifier(train)
cl = NaiveBayesClassifier(train)

# Classify some text
# print(cl.classify("Their burgers are amazing."))  # "pos"
# print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
# cl.show_informative_features(5)


#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                                          user="ustad", # your username
                                           passwd="ustad", # your password
                                           db="ustad") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM tips")

# print all the first cell of all the rows
for row in cur.fetchall() :
        print row[3]
