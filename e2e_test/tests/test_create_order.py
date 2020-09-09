import requests

#TODO
playload = {}

def test_create_order(url):
        response = requests.post(URL, data=playload)
            assert response == HTTP_STATUS.CREATED

