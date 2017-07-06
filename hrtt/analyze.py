# analyze.py
# interpret data from tweets


import nltk
import re


base_accounts = {}


def filter_tweets(status, keywords):
    """
    When a Status object is passed in, check its text against the list of
    keywords. If a match is found return True, otherwise return False.
    """
    # for x in range(len(keywords)):
    #     if keywords[x] in status.text.lower():  # match found
    #         return True
    # return False
    matches = 0
    max = 3

    for index, item in enumerate(keywords):
        if item in status.text.lower() and matches < max:
            matches += 1
        elif item in status.text.lower() and matches == max:
            return True
        elif index == len(keywords) and matches < max:
            return False

        return False


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)


def tokenize(status):
    tokens = tokens_re.findall(status.text)
    return dict([(status.author.screen_name, tokens)])
