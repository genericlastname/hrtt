import os
import sys
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
        keywords = kwf.read().splitlines()
        kwf.close()

        filtered = []  # tweets filtered by keywords
        # for x in range(len(tweets)):
        #     for y in range(len(keywords)):
        #         # if keywords[y] in tweets[x].text is False:
        #             filtered.append(tweets[x])
        #             print('Text: {}'.format(filtered[x].text))
        #             break

        for i in range(len(tweets)):
            matches = 0
            max = 2

            for index, item in enumerate(keywords):
                if item in tweets[i].text.lower() and matches < max:
                    matches += 1
                elif item in tweets[i].text.lower() and matches == max:
                    filtered.append(tweets[i])

            last = 0
            for i in range(1, len(tweets)):
                if tweets[i].text == tweets[last].text:
                    del(tweets[i])
                    last = i + 1

        if len(filtered) > 0:
            pf = open('data/filtered_tweets.pickle', 'wb+')
            pickle.dump(filtered, pf)
            pf.close()

        for x in range(len(filtered)):
            print(filtered[x].text)

        print('{} {}'.format(len(tweets), len(filtered)))

    elif args.command == 'view':
        # view filtered tweets conviently
        pf = open('data/filtered_tweets.pickle', 'rb')
        tweets = pickle.load(pf)
        pf.close()

        running = True

        c = 0

        while running:
            cmd = input('Enter number> ')

            if cmd == 'q':
                running = False
            elif cmd == '':
                print('{}: {}\n{}'.format(c,
                                          tweets[c].author.screen_name,
                                          tweets[c].text))
                c += 1
            else:
                c = int(cmd)
                if c > len(tweets) or c < 0:
                    print('Invalid range')
                else:
                    print('{}: {}\n{}'.format(c,
                                              tweets[c].author.screen_name,
                                              tweets[c].text))
                    c += 1
