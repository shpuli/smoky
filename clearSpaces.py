import requests
import json

url = 'https://preproduction.round.me/'

# Sign in credentials
superlogin = 'autotest4'
password = 'multipass'

headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

def authorize(login):
	payload = 'data%5Blogin%5D=' + login + '&data%5Bpassword%5D=' + password + '&data%5Bremember%5D=0'	
	r = requests.post(url + 'api/auth/login/', data=payload, headers=headers)
	authCookie = r.cookies['sid']
	cookies = dict(sid=authCookie)
	return cookies

cookies = authorize(superlogin)

r = requests.get(url + "api/tour/new?limit=100&start=0")
tours = r.json()
tours_to_delete = [tours['data'][x]['tour_id'] for x in range(100) if 'AutoCreated' in tours['data'][x]['name']]

for i in tours_to_delete:
	requests.delete(url + 'api/tour/bestnew/' + str(i), headers=headers, cookies=cookies)
	requests.delete(url + 'api/tour/editor/' + str(i), headers=headers, cookies=cookies)
	requests.delete(url + 'api/tour/' + str(i), headers=headers, cookies=cookies)
	