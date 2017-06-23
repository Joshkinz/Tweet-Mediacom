import urllib.request
import time
import twitter

def internet_on():
	try:
		urllib.request.urlopen('http://172.217.8.206', timeout=1)
		return True
	except urllib.request.URLError as err:
		return False
		
while True:
	a = internet_on()
	minute = 1
	if a == False:
		b = internet_on()
		while b == False:
			print("Internet offline for %i minutes." % minute)
			time.sleep(60)
			minute = minute + 1
		if b == True:
			print("Internet was out for %i minutes." % minute)
	if a == True:
		print("Internet is up at %i:%i:%i." % ())
		time.sleep(60)
