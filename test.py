# -*- coding: utf-8 -*-

from collections import Counter
from bs4 import BeautifulSoup

import nltk

import os
import re


def _stemming(word):
    return nltk.PorterStemmer().stem(word)

def get_stop_word(coll):
    # length of the collection
    l = len(coll.items())
    # percent number of words in the collection
    percent = (5 * l) / 100
    # sort collection by value
    sorted_dict = Counter(coll).most_common()
    # merge two part of collection
    stop_word_list = dict(sorted_dict[0:percent] + sorted_dict[l - (percent):l])

    return stop_word_list


def main():
    coll = {}

    for document in [f for f in os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), '1', 'documents'))]:
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '1', 'documents', document), 'r') as f:
            # tokenize document
            tokens = nltk.tokenize.word_tokenize(BeautifulSoup(f.read(), "lxml").get_text())
            for token in tokens:
                # remove symbols .,()
                if re.compile('\w').match(token):
                    # stemming, lower case and strip
                    token = _stemming(token.lower().strip())
                    # create dict with frequency. Can use FreqDist from nltk library
                    if coll.get(token, None):
                        coll[token] += 1
                    else:
                        coll[token] = 1

        # result dict with stop words
        print document + ' --- '
        print get_stop_word(coll)


if __name__ == '__main__':
    # download nltk data
    nltk.data.path.append('/Users/linar/PycharmProjects/nltk_data')
    # start main process
    main()