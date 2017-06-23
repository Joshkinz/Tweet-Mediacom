import urllib.request
import time

def internet_on():
	try:
		urllib.request.urlopen('https://172.217.8.206', timeout=1)
		print("True")
	except urllib.request.URLError as err:
		print("False")
		
while True:
	a = internet_on()
	minute = 1
	if a == False:
		b = internet_on()
		if b == False:
			print("Internet offline for %i minutes." % minute)
			time.sleep(1)
			minute = minute + 1
		if b == True:
			print("Internet was out for %i minutes." % minute)
	if a == True:
		print("Internet is up.")
