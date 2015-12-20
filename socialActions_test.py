__author__ = 'shpuli'
import random
from creds import *

usercookies = authorize(userlogin3)

def get_id_with_login(login):
	r = requests.get(url + "api/user/@" + login)
	user_id = r.json()['data'][0]['user_id']
	return str(user_id)

def get_last_tour_id(login):
	r = requests.get(url + "api/user/@" + login)
	tour_id = r.json()['data'][0]['toptours'][0]['tour_id']
	return str(tour_id)


def test_follow():
	r = requests.post(url + "api/user/" + get_id_with_login(userlogin) + "/follow", cookies = usercookies)
	assert r.status_code == 200, 'Wrong status_code after following ' + r.text
	r = requests.delete(url + "api/user/" + get_id_with_login(userlogin) + "/follow", cookies = usercookies)
	assert r.status_code == 200, 'Wrong status_code after unfollowing ' + r.text

def test_like():
	r = requests.post(url + "api/tour/" + get_last_tour_id(userlogin) + "/favorite", cookies = usercookies)
	assert r.status_code == 200, 'Wrong status_code after like ' + r.text
	r = requests.delete(url + "api/tour/" + get_last_tour_id(userlogin) + "/favorite", cookies = usercookies)
	assert r.status_code == 200, 'Wrong status_code after like ' + r.text