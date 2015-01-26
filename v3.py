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
import random
import re
import nltk

groups = {
        # 'dunya': {
        #     'min_id': 1,
        #     'max_id': 3724
        # },
        'ekonomi': {
            'min_id': 3725,
            'max_id': 6989,
        },
        # 'genel': {
        #     'min_id': 6990,
        #     'max_id': 13660,
        # },
        # 'guncel': {
        #     'min_id': 13661,
        #     'max_id': 19507,
        # },
        'kultur-sanat': {
            'min_id': 19508,
            'max_id': 20662
        },
        # 'magazin': {
        #     'min_id': 20663,
        #     'max_id': 23454
        # },
        # 'planet': {
        #     'min_id': 23455,
        #     'max_id': 25407
        # },
        'saglik': {
            'min_id': 25408,
            'max_id': 26790
        },
        'siyaset': {
            'min_id':  26791,
            'max_id': 28639
        },
        'spor': {
            'min_id': 28640,
            'max_id': 38636
        },
        # 'teknoloji': {
        #     'min_id': 38637,
        #     'max_id': 39407
        # },
        # 'turkiye': {
        #     'min_id': 39408,
        #     'max_id': 41346
        # },
        # 'yasam': {
        #     'min_id': 41347,
        #     'max_id': 41990
        # }
}

def extractor(doc):
    tokens = doc.split()

    features = {}

    for token in tokens:
        if len(token) < 3:
            continue
        if token in stop_words_turkish:
            continue

        token = re.sub("\'|\"|\.|\,|\;|\:|\*|\?|\!|\-", "", token)

        features[token] = True

    return features


all_set = []
stop_words_turkish = []

with open('stop-words-turkish.txt') as file:
    for line in file:
        stop_words_turkish.append(line.strip())


db = MySQLdb.connect(host="localhost", user="test", passwd="test", db="test")
cur = db.cursor()
train_set = []

for key in groups:
    record_count = 500
    group = groups[key]
    cur.execute("SELECT title, content, class_name FROM data WHERE class_name = '%s' LIMIT %d" % (key, record_count))

    for row in cur.fetchall():
        text = unicode(str(row[0]) + ' ' + str(row[1]), 'utf-8')
        all_set.append((text, key))

# tüm verileri karıştır
random.shuffle(all_set)

total = 500
use_set = all_set[0:total]
slice_group = 5
each_group_count = total / slice_group
accuracy = 0


for i in range(slice_group):
    train_set = use_set[0 : i * each_group_count] + use_set[(i + 1) * each_group_count :]
    test_set = use_set[i * each_group_count : (i + 1) * each_group_count]

    # totals = {}
    #
    # for i in train_set:
    #     status = i[1]
    #     if status in totals.keys():
    #         totals[status] = totals[status] + 1
    #     else:
    #         totals[status] = 1
    #
    # print "eğitim:"
    # for i in totals:
    #     print "%d: %s" %(totals[i], i)
    #
    # print "--------------------------------------------------------------------"
    #
    # totals = {}
    #
    # for i in test_set:
    #     status = i[1]
    #     if status in totals.keys():
    #         totals[status] = totals[status] + 1
    #     else:
    #         totals[status] = 1
    #
    # print "test:"
    # for i in totals:
    #     print "%d: %s" %(totals[i], i)
    #
    # print "--------------------------------------------------------------------"

    print "eğitim verisi sayısı: %d" % len(train_set)
    print "test_set verisi sayısı: %d" % len(test_set)
    print "ağ eğitiliyor..."

    # cl = DecisionTreeClassifier(train_set)
    # cl = DecisionTreeClassifier(train_set, feature_extractor=extractor)
    # cl = MaxEntClassifier(train_set)
    # cl = MaxEntClassifier(train_set, feature_extractor=extractor)
    # cl = NaiveBayesClassifier(train_set)
    cl = NaiveBayesClassifier(train_set, feature_extractor=extractor)
    # cl.show_informative_features(10)
    print "test ediliyor..."

    accuracy_ = cl.accuracy(test_set)
    accuracy += accuracy_
    print "Doğruluk: %.2f" %(accuracy_)
    print "----------------------------"

# ağın doğruluğunu hesapla
print "\nDoğruluk: %.2f" %(accuracy / slice_group)
