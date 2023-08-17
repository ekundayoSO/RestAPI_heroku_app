import pprint

import requests

import Utilities.Generic

base_url = "https://restful-booker.herokuapp.com"


def post_request():
    url = base_url + "/booking"
    headers = {"Content-Type": "application/json"}

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
            "additionalneeds": "Lunch meal"
        }

    resp = requests.post(url, json=body, headers=headers)
    status_code = resp.status_code
    json_data = resp.json()
    print(status_code)
    pprint.pprint(json_data)
    booking_id = json_data["bookingid"]

    return booking_id


booking_id = post_request()
