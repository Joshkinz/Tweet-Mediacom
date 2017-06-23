import urllib2
import time

def internet_on():
	try:
		urllib2.urlopen('https://172.217.8.206', timeout=1)
		return True
	except urllib2.URLError as err:
		return False
		
while True:
	a = internet_on()
	minute = 1
	while a == False:
		b = internet_on()
		if b == False:
			print("Internet offline for %i minutes." % minute)
			time.sleep(1)
			minute = minute + 1
		if b == True:
			a = True
	if a == True:
		print("Internet was out for %i minutes." % minute)
