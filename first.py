#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sudo apt-get install python-pip python-mysqldb
# pip install -U textblob
# python -m textblob.download_corpora

from textblob.classifiers import BaseClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob.classifiers import MaxEntClassifier
from textblob.classifiers import NaiveBayesClassifier
from textblob.blob import TextBlob
import MySQLdb


db = MySQLdb.connect(host="localhost", user="test", passwd="test", db="test")
cur = db.cursor()
cur.execute("SELECT title, content, class_name FROM data limit 50")

train = []
for row in cur.fetchall():
    text = unicode(str(row[0]) + ' ' + str(row[1]), 'utf-8')
    train.append((text, row[2]))


cur.execute("SELECT title, content, class_name FROM data limit 5 offset 20")

test = []
for row in cur.fetchall():
    text = unicode(str(row[0]) + ' ' + str(row[1]), 'utf-8')
    test.append((text, row[2]))




# cl = BaseClassifier(train)
# cl = DecisionTreeClassifier(train)
# cl = MaxEntClassifier(train)
cl = NaiveBayesClassifier(train)

# Classify some text
# print(cl.classify("Their burgers are amazing."))  # "pos"
# print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("\nAccuracy: {0}".format(cl.accuracy(test)))
