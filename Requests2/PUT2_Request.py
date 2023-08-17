import requests

import Token.Authentication
import Utilities.Generic
from Requests2.POST2_Request import booking_ids

base_url = "https://restful-booker.herokuapp.com"
token = Token.Authentication.generateAuthenticationToken()


def put_request(booking_ids):
    url = base_url + "/booking"
    print("PUT url:" + url)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

    data = [
        {
            "firstname": "Sulaimon",
            "lastname": Utilities.Generic.generateLastName(),
            "totalprice": 200,
            "depositpaid": False,
            "bookingdates":
                {
                    "checkin": "2023-08-23",
                    "checkout": "2024-10-23"
                },
            "additionalneeds": "Dinner"
        },
        {
            "firstname": "Felix",
            "lastname": Utilities.Generic.generateLastName(),
            "totalprice": 170,
            "depositpaid": True,
            "bookingdates":
                {
                    "checkin": "2023-08-23",
                    "checkout": "2024-10-23"
                },
            "additionalneeds": "Lunch"
        },
        {
            "firstname": "Duke",
            "lastname": Utilities.Generic.generateLastName(),
            "totalprice": 288,
            "depositpaid": True,
            "bookingdates":
                {
                    "checkin": "2023-08-23",
                    "checkout": "2024-10-23"
                },
            "additionalneeds": "Breakfast"
        },
    ]

    for booking_id, updated_data in zip(booking_ids, data):
        url_with_id = f"{url}/{booking_id}"
        resp = requests.put(url_with_id, json=updated_data, headers=headers)
        json_data = resp.json()
        assert resp.status_code == 200
        firstnames = json_data["firstname"]
        print(firstnames)


put_request(booking_ids)
