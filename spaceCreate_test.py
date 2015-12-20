__author__ = 'shpuli'
import random
from creds import *

rand = random.randint(1000, 9999)
name = 'api created space' + str(rand)
description = 'api created description'
picture = {'file': open('TestPanorams/panorama.jpg', 'rb')}

authorcookies = authorize(userlogin3)

def test_space_create():
	r = requests.post(url + "api/panorama/upload", files = picture, cookies=authorcookies)

	assert r.status_code == 200, 'Wrong status_code after picture post ' + r.text

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

	r = requests.post(url + "api/tour", cookies=authorcookies, data=json.dumps(payload))

	assert r.status_code == 200, 'Wrong status_code after space creation ' + r.text

	tour = r.json()

	assert tour['data']['name']==name
	assert tour['data']['description']==description
	assert tour['data']['location']=='Candesti, Romania'
	assert tour['data']['categories'][0]['name']=='Food'

	tour_id = tour['data']['tour_id']

	r = requests.delete(url +  "api/tour/" + str(tour_id), cookies=authorcookies)

	assert r.status_code == 200, 'Wrong status_code after space deletion ' + r.text
