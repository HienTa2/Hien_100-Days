import json
from datetime import datetime
import requests

MY_LAT = 33.112559
MY_LONG = -96.913164


def is_iss_overhear():
    # API endpoint ISS
    endpoint = 'http://api.open-notify.org/iss-now.json'

    response = requests.get(url=endpoint)
    response.raise_for_status()
    data = response.json()
    print(data)

    # ISS position. Get the key to show the values
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    # Check if ISS position is near my position
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long + 5:
        return True


if is_iss_overhear():
    print("Look up!")
