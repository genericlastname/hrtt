# HRTT
## Health Rumor Tweet Tracker

### Requirements
* tweepy

### Running
To download the ids for all twitter accounts in 'data/accounts.txt' execute

    ./run.py scrape

The ids will be stored in 'data/tweet_ids.txt'.

Next execute

    ./run.py save

To save the tweets in the binary file 'data/tweets.pickle'. Careful, this process
takes a **VERY** long time to complete.

Now execute

    ./run.py filter

to filter the saved tweets by the keywords in 'data/keywords.txt'. The filtered
tweets will be stored in the binary file 'data/filtered_tweets.pickle'.

Finally to view the filtered tweets execute

    ./run.py view
