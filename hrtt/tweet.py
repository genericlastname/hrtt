# tweet.py


from .globals import _api


def load_tweets(path='data/tweet_ids.txt'):
    """Load in tweet ids, return list of status objects"""
    with open(path) as f:
        ids = f.readlines()
        ids = [x.strip() for x in ids]
        status = []

        print('{} ids to load.'.format(len(ids)))
        for x in range(len(ids)):
            obj = _api.get_status(ids[x])
            status.append(obj)
            print('{}) Loaded tweet with id: {}'.format(x+1, ids[x]))

        return status
