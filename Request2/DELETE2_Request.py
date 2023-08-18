import requests

import Token.Authentication
from Request2.POST2_Request import booking_ids

base_url = "https://restful-booker.herokuapp.com"
token = Token.Authentication.generateAuthenticationToken()


def delete_request(booking_ids):
    url = base_url + "/booking"
    print("PUT url:" + url)

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    for booking_id in booking_ids:
        url = f"{base_url}/booking/{booking_id}"
        response = requests.delete(url, headers=headers)

        assert response.status_code == 201


delete_request(booking_ids)