#!/usr/bin/env python

import tweepy, time, sys
from secrets import *

# argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET_TOKEN)
api = tweepy.API(auth)

filename = 'glitch1.jpg'
message = "Good Glitchez"
api.update_with_media(filename, status=message)
