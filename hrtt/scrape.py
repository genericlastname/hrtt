# scrape.py
# Functions to collect tweets from specific twitter accounts


from .globals import _api


def load_accounts(path):
    """Load in twitter accounts from a file and return a list"""
    with open(path, 'r') as f:
        acc = [x.strip() for x in f.readlines()]
        return acc


def scrape_from_user(acc, num, path='data/tweet_ids.txt'):
    """Collect tweets from account in `acc` and save them in the file
       `path`"""
    print('Collecting tweets from {}'.format(acc[num]))

    tweets = []
    new_tweets = []

    # new_tweets = _api.user_timeline(screen_name=acc[num], count=200)
    new_tweets = _api.user_timeline(screen_name=acc[num], count=5)
    tweets.extend(new_tweets)

    # oldest = tweets[-1].id - 1

    # while len(new_tweets) > 0:
    #     new_tweets = _api.user_timeline(screen_name=acc[num], count=200,
    #                                     max_id=oldest)
    #     tweets.extend(new_tweets)
    #     oldest = tweets[-1].id - 1
    #     print('{} tweets collected so far'.format(len(tweets)), end='\r')

    with open(path, 'a+') as f:
        for x in range(len(tweets)):
            f.write(str(tweets[x].id_str))
            f.write('\n')

    print('\nDone.')
