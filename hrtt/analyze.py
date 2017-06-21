# analyze.py
# interpret data from tweets


def filter_tweets(status, keywords):
    """
    When a Status object is passed in, check its text against the list of
    keywords. If a match is found return True, otherwise return False.
    """
    for x in range(len(keywords)):
        if keywords[x] in status.text:  # match found
            return True
    return False
