import os
import argparse
from .scrape import load_accounts
from .scrape import scrape_from_user
from .tweet import load_tweets
from .analyze import filter_tweets
import pickle


def cleanup():
    """Remove tweets.json"""
    os.remove('data/tweet_ids.txt')


def main():
    parser = argparse.ArgumentParser(description='Analyze Twitter data')
    parser.add_argument('command', help='what subprogram hrtt should run')
    args = parser.parse_args()

    if args.command == 'clean':
        cleanup()

    elif args.command == 'scrape':
        acc = load_accounts('data/accounts.txt')
        for x in range(len(acc)):
            print('Account {}'.format(x+1))
            scrape_from_user(acc, x)

    elif args.command == 'save':
        tweets = load_tweets('data/tweet_ids.txt')
        with open('data/tweets.pickle', 'wb+') as f:
            pickle.dump(tweets, f)

    elif args.command == 'filter':
        pf = open('data/tweets.pickle', 'rb')
        tweets = pickle.load(pf)
        pf.close()

        kwf = open('data/keywords.txt')  # keyword file
        keywords = kwf.readlines()
        kwf.close()

        filtered = []  # tweets filtered by keywords

        for x in range(len(tweets)):
            if filter_tweets(tweets[x], keywords):
                filtered.append(tweets[x])
                print('Match found for tweet {}.'.format(tweets[x].id_str))

        if len(filtered) > 0:
            pf = open('data/filtered_tweets.pickle', 'wb+')
            pickle.dump(filtered, pf)
            pf.close()


# def main():
#     if len(sys.argv) < 2:
#         print('Not enough arguments!')
#     elif len(sys.argv) >= 2:
#         if sys.argv[1] == 'cleanup':
#             cleanup()
#         elif sys.argv[1] == 'scrape':
#             acc = load_accounts('data/accounts.txt')
#             for x in range(len(acc)):
#                 print('Account {}'.format(x+1))
#                 scrape_from_user(acc, x)
#         elif sys.argv[1] == 'save':
#             tweets = load_tweets('data/tweet_ids.txt')
#             print(tweets)
#             with open('data/tweets.pickle', 'wb+') as f:
#                 pickle.dump(tweets, f)
#         elif sys.argv[1] == 'load':
#             with open('data/tweets.pickle') as f:
#                 tweets = pickle.load(f)
#         else:
#             print('Not a recognized argument')
