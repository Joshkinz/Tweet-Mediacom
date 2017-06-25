import urllib.request
import time
import twitter
import datetime

# Last updated 6/24/2017
GOOGLE_IP = 'http://172.217.8.206'
MEDIACOMCABLE_IP = 'http://68.66.66.193'
REDDIT_IP = 'http://151.101.1.140'

#--Connect to Twitter

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

#--Defines the check for internet

def internet_on():
	for _ in range(15):
		try:
			urllib.request.urlopen(GOOGLE_IP, timeout=5)
			return True
		except urllib.request.URLError:
			pass
	return False

#--Checks if internet is up, tweets if not

while True:
	a = internet_on()
	minute = 0
	while not a:
		b = internet_on()
		if not b:
			print("Internet offline for %i minutes at %s." % (minute, datetime.datetime.now()))
			time.sleep(120)
			minute += 2
		else:
			print("Internet was out for %i minutes, back up at %s." % (minute, datetime.datetime.now()))
			if minute > 2:
				api.PostUpdate("Hey @MediacomSupport my internet was out for %i minutes. It has been going out for several minutes on a daily basis #mediacom #internet" % minute)
			a = True
			time.sleep(120)
	if a:
		print("Internet is up at %s." % datetime.datetime.now())
		time.sleep(120)
