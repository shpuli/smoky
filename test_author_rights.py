import random
from creds import *

rand = random.randint(1000, 9999)
name = 'api created space' + str(rand)
description = 'api created description'
picture = {'file': open('TestPanorams/panorama.jpg', 'rb')}

authorcookies = authorize(authorlogin)
supercookies = authorize(superlogin)
usercookies = authorize(userlogin)

def spaceCreate():
	r = requests.post(url + 'api/panorama/upload', files = picture, cookies=authorcookies)
	data = (r.json()['data']['filename'])
	payload = {
		'name': name,
		'is_draft': False,
		'panoramas': [{
			'name':'',
			'filename': data
		}],
		'categoriesBind':[1,4],
		'description': description,
		'location_zoom': 4,
		'is_disabled_pano_list': True,
		'is_disabled_comments': True,
		'location': 'Candesti, Romania',
		'lat': 45.058001435398296,
		'lon': 25.13671875
	}
	r = requests.post(url + 'api/tour', cookies=authorcookies, data=json.dumps(payload))
	tour = r.json()
	tour_id = tour['data']['tour_id']
	return tour_id

tour_id = spaceCreate()

def get_tour_json():
	r = requests.get(url + 'api/tour/' + str(tour_id))
	tour = r.json()
	return tour

#return cookies, tour_id
testdata = [(authorcookies, 403, 0, authorlogin),
			 (usercookies, 403, 0, userlogin),
			 (supercookies, 200, 1, superlogin)
			 ]

@pytest.mark.parametrize("cookies,expected_code,expected_state,login", testdata)
def test_author_cannot_add_editors(cookies,expected_code,expected_state,login):
	r = requests.put(url +  'api/tour/editor/' + str(tour_id), cookies=cookies)
	assert r.status_code == expected_code, 'Failed on ' + login + ': ' + r.text
	tour = get_tour_json()
	assert tour['data']['for_editor']==expected_state, 'Wrong tour data for ' + login

@pytest.mark.parametrize("cookies,expected_code,expected_state,login", testdata)
def test_author_cannot_add_bestnew(cookies,expected_code,expected_state,login):
	r = requests.put(url +  'api/tour/bestnew/' + str(tour_id), cookies=cookies)
	assert r.status_code == expected_code, 'Failed on ' + login + ': ' + r.text
	tour = get_tour_json()
	assert tour['data']['for_new']==expected_state, 'Wrong tour data for ' + login

@pytest.mark.parametrize("cookies,expected_code,expected_state,login", testdata)
def test_author_cannot_hide(cookies,expected_code,expected_state,login):
	r = requests.delete(url +  'api/tour/' + str(tour_id) + '/visibility', cookies=cookies)
	assert r.status_code == expected_code, 'Failed on ' + login + ': ' + r.text
	tour = get_tour_json()
	assert tour['data']['is_hidden']==bool(expected_state), 'Wrong tour data for ' + login

@pytest.mark.parametrize("cookies,expected_code,expected_state,login", testdata)
def test_author_cannot_unhide(cookies,expected_code,expected_state,login):	
	r = requests.delete(url +  'api/tour/' + str(tour_id) + '/visibility', cookies=supercookies)
	tour = get_tour_json()
	assert tour['data']['is_hidden']==True, 'Space is not hidden!'
	r = requests.put(url +  'api/tour/' + str(tour_id) + '/visibility', cookies=cookies)
	assert r.status_code == expected_code, 'Failed on ' + login + ': ' + r.text
	tour = get_tour_json()
	assert tour['data']['is_hidden'] != bool(expected_state), 'Wrong tour data for ' + login

#r = requests.delete(url +  "api/tour/" + str(tour_id), cookies=authorcookies)