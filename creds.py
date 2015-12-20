import pytest
import requests
import json

url = 'https://preproduction.round.me/'

# Sign in credentials
authorlogin = 'autotest1'
userlogin = 'autotest2'
userlogin3 = 'autotest3'
superlogin = 'autotest4'
password = 'multipass'

def authorize(login):
	payload = 'data%5Blogin%5D=' + login + '&data%5Bpassword%5D=' + password + '&data%5Bremember%5D=0'	
	headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	r = requests.post(url + 'api/auth/login/', data=payload, headers=headers)
	if (r.status_code != 200): raise Exception("Cannot login: " + login + " " + password + " " + str(r.status_code))
	authCookie = r.cookies['sid']
	cookies = dict(sid=authCookie)
	return cookies