#!/usr/local/bin/python3

import requests

URL="https://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
user="XXXXXXXXXXXXXXXXXXXX"
password="XXXXXXXXXXXXXXXX"

proxies = { 
	"http": "http://127.0.0.1:8080",
	"https": "http://127.0.0.1:8080",
}

	
print("Logging into: "+URL)

payload = "username="+user+"&password="+password

custom_header = {
	'Content-Type': 'application/x-www-form-urlencoded'
}


r = requests.post(URL, data=payload, headers=custom_header, proxies=proxies, verify=False, allow_redirects=False)
	#allow_redirects=False is used to ignore the 302 redirect in order to get the cookies in the server response
	#Set allow_redirects=True to automatically following the redirect

for cookie in r.cookies:
	print('cookie domain = ' + cookie.domain)
	print('cookie name = ' + cookie.name)
	print('cookie value = ' + cookie.value)
	print('***************************************')




	




