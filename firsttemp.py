from twill.commands import *
from twill import *
from twill import namespaces
browser = get_browser()
url = "http://clients.sribnyj.com.ua/test/"
browser.go(url)
formclear('1')
fv("1", "UserLogin", "aleksey")
fv("1", "UserPassword", "aleksey")
submit()
try:
    find("Bad Karma","m")
except:
	try:
		find("Well Done","m")
	except:
		print "Sorry, but some error occured"
	else:
		print "Welcome to matrix, Neo"
else:
	print "Sorry, wrong login and password"