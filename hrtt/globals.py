# globals.py
# holds important vars


import tweepy


# tweepy globals
_ck = 'wka2iuZW3Aky7SFhwA8PhAGnl'
_cs = 'Swqq8AgjFRnKTEg3gmyBJDUZ8fnzqdfhfDirhn8owj0czog2vf'
_ak = '869984091692822528-ykmxl5GO0FnISwSXjLMGmTC6FOvmgkU'
_as = 'vUR9RmBvmAu5EJI2ijZKHBFfJafMpkI6EoDxulNvsigK5'

_auth = tweepy.OAuthHandler(_ck, _cs)
_auth.set_access_token(_ak, _as)
_api = tweepy.API(_auth, wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)
