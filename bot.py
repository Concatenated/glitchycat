#!/usr/bin/env python

import tweepy, time, sys
from secrets import *

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET_TOKEN)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(900)
