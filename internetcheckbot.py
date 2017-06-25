import urllib.request
import time
import datetime
import random
import json

import twitter


# Last updated 6/24/2017
GOOGLE_IP = 'http://172.217.8.206'
MICROSOFT_IP = 'http://104.40.211.35'
REDDIT_IP = 'http://151.101.1.140'
IP_ADDRESSES = [GOOGLE_IP, MICROSOFT_IP, REDDIT_IP]

# The maximum attempts to ping the above IP adresses before declaring internet as off
MAXIMUM_ATTEMPTS = 15

# Get login info from config
with open('config.json') as file:
    config = json.load(file)

# Connect to Twitter
api = twitter.Api(consumer_key=config['consumer-key'],
	consumer_secret=config['consumer-secret'],
	access_token_key=config['access-token']['key'],
	access_token_secret=config['access-token']['secret'])

# Defines the check for internet
def internet_on():
	for _ in range(MAXIMUM_ATTEMPTS):
		try:
			urllib.request.urlopen(random.choice(IP_ADDRESSES), timeout=5)
			return True
		except urllib.request.URLError:
			pass
	return False

# Checks if internet is up, tweets if not
while True:
	currently_online = internet_on()
	minute = 0
	while not currently_online:
		if not internet_on():
			print("Internet offline for %i minutes at %s." % (minute, datetime.datetime.now()))
			time.sleep(120)
			minute += 2
		else:
			print("Internet was out for %i minutes, back up at %s." % (minute, datetime.datetime.now()))
			if minute > 2:
				api.PostUpdate("Hey @MediacomSupport my internet was out for %i minutes. It has been going out for several minutes on a daily basis #mediacom #internet" % minute)
			currently_online = True
			time.sleep(120)
	print("Internet is up at %s." % datetime.datetime.now())
	time.sleep(120)
