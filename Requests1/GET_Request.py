import pprint

import requests

base_url = "https://restful-booker.herokuapp.com"


def get_request():
    url = base_url + "/booking"
    resp = requests.get(url)
    status_code = resp.status_code
    json_data = resp.json()
    print(status_code)
    pprint.pprint(json_data)


def get_request2():
    url = base_url + "/booking/4930"
    resp = requests.get(url)
    assert resp.status_code == 200
    json_data = resp.json()
    assert json_data["firstname"] == "Sulaimon"
    pprint.pprint(json_data["lastname"])
    pprint.pprint(json_data)


get_request()
# test_get_request2()
