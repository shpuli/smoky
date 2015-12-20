__author__ = 'shpuli'
import random
from creds import *

newpassword = "newpass"
authorcookies = authorize(userlogin3)
authorcookies_to_change = authorize(userlogin3)

def get_id_with_login(login):
	r = requests.get(url + "api/user/@" + login)
	user = r.json()
	user_id = user['data'][0]['user_id']
	return str(user_id)

def change_pass(oldpass, newpass):
	payload = {
		'current_password': oldpass,
		'password': newpass
	}
	r = requests.put(url + "api/user/changepassword", cookies=authorcookies_to_change, data=json.dumps(payload))

change_pass(password, newpassword)

def test_follow():
	r = requests.post(url + "api/user/" + get_id_with_login(userlogin) + "/follow", cookies = authorcookies)
	assert r.status_code == 404, 'Wrong status_code after following ' + r.text

change_pass(newpassword, password)