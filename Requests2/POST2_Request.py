import pprint

import requests

import Utilities.Generic

base_url = "https://restful-booker.herokuapp.com"


def post_request():
    url = base_url + "/booking"
    print("POST url:" + url)
    headers = {"Content-Type": "application/json"}

    data = [
        {
            "firstname": "Sulaimon",
            "lastname": Utilities.Generic.generateLastName(),
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates":
                {
                    "checkin": "2023-08-23",
                    "checkout": "2024-10-23"
                },
            "additionalneeds": "Breakfast"
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
            "additionalneeds": "Dinner"
        },
    ]

    booking_ids = []
    for body in data:
        resp = requests.post(url, json=body, headers=headers)
        status_code = resp.status_code
        json_data = resp.json()
        print(status_code)
        pprint.pprint(json_data)
        booking_id2 = json_data["bookingid"]

        booking_ids.append(booking_id2)
        print(booking_ids)

    return booking_ids


booking_ids = post_request()



