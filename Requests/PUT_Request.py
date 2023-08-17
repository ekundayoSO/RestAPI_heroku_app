import pprint

import requests

import Token.Authentication
import Utilities.Generic
from Requests.POST_Request import booking_id

base_url = "https://restful-booker.herokuapp.com"
token = Token.Authentication.generateAuthenticationToken()


def put_request(booking_id):
    url = base_url + f"/booking/{booking_id}"
    print("PUT url:" + url)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    body = {
        "firstname": "Sulaimon",
        "lastname": Utilities.Generic.generateLastName(),
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates":
            {
                "checkin": "2023-08-23",
                "checkout": "2024-10-23"
            },
        "additionalneeds": "Lunch & Dinner"
    }

    resp = requests.put(url, headers=headers, json=body)
    status_code = resp.status_code
    json_data = resp.json()
    print(status_code)
    pprint.pprint(json_data)


put_request(booking_id)
