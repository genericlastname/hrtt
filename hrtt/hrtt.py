import sys
import os
from .scrape import load_accounts
from .scrape import scrape_from_user


def cleanup():
    """Remove tweets.json"""
    os.remove('data/tweets.json')


def main():
    if len(sys.argv) < 2:
        print('Not enough arguments!')
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'cleanup':
            cleanup()
        elif sys.argv[1] == 'scrape':
            acc = load_accounts('data/accounts.txt')
            for x in range(len(acc)):
                print('Account {}'.format(x+1))
                scrape_from_user(acc, x)
        else:
            print('Not a recognized argument')
