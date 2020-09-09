import requests

URL = "http://www.google.com"

def test_smoke():
    response = requests.get(URL)
    assert response.status_code == 200
