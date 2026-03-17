"""
this script creatres new user on real world conduit app. You can sue this user to access the app.
"""

import requests
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
register_payload ={
    "user": {
        "username": "sergiu_verlan",
        "email": os.getenv("TEST_USER_EMAIL"),
        "password": os.getenv("TEST_USER_PASSWORD")
    }
}
rs = requests.post(
    f"{BASE_URL}/users",
    json=register_payload,
    headers={"Content-Type": "application/json"}
)
print(f"Status code: {rs.status_code}")
print(f"Response: {rs.json()}")
