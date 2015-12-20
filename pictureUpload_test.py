import random
from creds import *

rand = random.randint(1000, 9999)
name = 'api created space' + str(rand)
description = 'api created description'
picture = {'file': open('TestPanorams/panorama.jpg', 'rb')}

authorcookies = authorize(authorlogin)

jpeg = {'file': open('TestPanorams/panorama.jpg', 'rb')}
tiff = {'file': open('TestPanorams/tiffpanorama.tif', 'rb')}
nonpano = {'file': open('TestPanorams/pngpict.png', 'rb')}
faketiff = {'file': open('TestPanorams/faketiff.tiff', 'rb')}
fakejpg = {'file': open('TestPanorams/fakejpg.jpg', 'rb')}
bigjpg = {'file': open('TestPanorams/bigpanorama.jpg', 'rb')}

test_data = [(jpeg, 200),
			 (tiff, 200),
			 (nonpano, 400),
			 (faketiff, 400),
			 (fakejpg, 400),
			 (bigjpg, 400)
			 ]

@pytest.mark.parametrize("picture, expected_state", test_data)
def test_picture_upload(picture, expected_state):
	r = requests.post(url + 'api/panorama/upload', files = picture, cookies=authorcookies)
	assert r.status_code == expected_state, r.text
	if r.status_code==200:
		assert r.json()['data']['filename'] != ''
	elif r.status_code==400:
		assert r.json()['name'] == 'ValidationError'
