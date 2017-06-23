import urllib.request
import time
import twitter
import datetime

#--Connect to Twitter

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

#--Defines the check for internet

def internet_on():
	try:
		urllib.request.urlopen('http://172.217.8.206', timeout=1)
		#172.217.8.206 is google's IP
		return True
	except urllib.request.URLError as err:
		return False

#--Checks if internet is up, tweets if not

while True:
	a = internet_on()
	minute = 1
	while a == False:
		b = internet_on()
		if b == False:
			print("Internet offline for %i minutes at %s." % (minute, datetime.datetime.now()))
			time.sleep(60)
			minute = minute + 1
		if b == True:
			print("Internet was out for %i minutes, back up at %s." % (minute, datetime.datetime.now()))
			if minute > 2:
				api.PostUpdate("@MediacomSupport My internet was out for %i minutes. We've now had 3 technicians out with no fix. (This is a bot written by @Joshkinz_ )" % minute)
			a = True
			time.sleep(60)
	if a == True:
		print("Internet is up at %s." % datetime.datetime.now())
		time.sleep(60)
