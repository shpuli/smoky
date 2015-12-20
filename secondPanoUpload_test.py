import random
from creds import *

rand = random.randint(1000, 9999)
name = 'api created space' + str(rand)
description = 'api created description'
picture = {'file': open('TestPanorams/panorama.jpg', 'rb')}

authorcookies = authorize(authorlogin)

r = requests.post(url + "api/panorama/upload", files = picture, cookies=authorcookies)
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
tour_id = r.json()['data']['tour_id']

def pano_upload_test():
	r = requests.post(url + '/api/panorama/upload', )