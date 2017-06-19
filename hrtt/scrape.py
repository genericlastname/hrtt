# scrape.py
# Functions to collect tweets from specific twitter accounts


import tweepy


# tweepy globals
_ck = 'wka2iuZW3Aky7SFhwA8PhAGnl'
_cs = 'Swqq8AgjFRnKTEg3gmyBJDUZ8fnzqdfhfDirhn8owj0czog2vf'
_ak = '869984091692822528-ykmxl5GO0FnISwSXjLMGmTC6FOvmgkU'
_as = 'vUR9RmBvmAu5EJI2ijZKHBFfJafMpkI6EoDxulNvsigK5'


def load_accounts(path):
    """Load in twitter accounts from a file and return a dict"""
    with open(path, 'r') as f:
        acc = [x.strip() for x in f.readlines()]
        return acc


def scrape_from_user(acc, num, path='data/tweets.json'):
    """Collect tweets from account in `acc` and save them in the file
       `path`"""
    print('Collecting tweets from {}'.format(acc[num]))

    auth = tweepy.OAuthHandler(_ck, _cs)
    auth.set_access_token(_ak, _as)
    api = tweepy.API(auth)

    tweets = []
    new_tweets = []

    new_tweets = api.user_timeline(screen_name=acc[num], count=200)
    tweets.extend(new_tweets)

    oldest = tweets[-1].id - 1

    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=acc[num], count=200,
                                       max_id=oldest)
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1
        print('{} tweets collected so far'.format(len(tweets)), end='\r')

    with open(path, 'a+') as f:
        for x in range(len(tweets)):
            f.write(str(tweets[x]._json))

    print('\nDone.')
