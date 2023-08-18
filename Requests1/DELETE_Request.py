import requests

import Token.Authentication
from Requests1.POST_Request import booking_id

base_url = "https://restful-booker.herokuapp.com"
token = Token.Authentication.generateAuthenticationToken()


def delete_request(booking_id):
    url = base_url + f"/booking/{booking_id}"
    print("DELETE url:" + url)
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    response = requests.delete(url, headers=headers)
    print(response.status_code)
    assert response.status_code == 201


delete_request(booking_id)
