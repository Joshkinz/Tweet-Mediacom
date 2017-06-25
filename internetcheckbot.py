import urllib.request
import time
import twitter
import datetime

#--Connect to Twitter

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

#--Defines the check for internet

def internet_on():
	attempts = 5
	while attempts > 0:
		try:
			urllib.request.urlopen('http://172.217.8.206', timeout=5)
			#172.217.8.206 is google.com's IP (as of 6/24/2017)
			return True
			break
		except urllib.request.URLError as err:
			attempts = attempts -1
	if attempts == 0:
		attempts2 = 5
		while attempts2 > 0:
			try:
				urllib.request.urlopen('http://68.66.66.193', timeout=5)
				#68.66.66.193 is mediacomcable.com's IP (as of 6/24/2017)
				return True
				break
			except urllib.request.URLError as err:
				attempts2 = attempts2 - 1
		if attempts2 == 0:
			attempts3 = 5
			while attempts3 > 0:
				try:
					urllib.request.urlopen('http://151.101.1.140', timeout=5)
					#151.101.1.140 is reddit.com's IP (as of 6/24/2017)
					return True
					break
				except urllib.request.URLError as err:
					attempts3 = attempts3 - 1
			if attempts3 == 0:
				return False

#--Checks if internet is up, tweets if not

while True:
	a = internet_on()
	minute = 0
	while a == False:
		b = internet_on()
		if b == False:
			print("Internet offline for %i minutes at %s." % (minute, datetime.datetime.now()))
			time.sleep(120)
			minute = minute + 2
		if b == True:
			print("Internet was out for %i minutes, back up at %s." % (minute, datetime.datetime.now()))
			if minute > 2:
				api.PostUpdate("Hey @MediacomSupport my internet was out for %i minutes. It has been going out for several minutes on a daily basis #mediacom #internet" % minute)
			a = True
			time.sleep(120)
	if a == True:
		print("Internet is up at %s." % datetime.datetime.now())
		time.sleep(120)
