import os
import argparse
from .scrape import load_accounts
from .scrape import scrape_from_user
from .tweet import load_tweets
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

    elif args.command == 'load':
        with open('data/tweets.pickle', 'rb') as f:
            tweets = pickle.load(f)
            print('{} {}'.format(tweets[2].author.name, tweets[2].text))


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
