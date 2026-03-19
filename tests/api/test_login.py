import pytest
import requests
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("TEST_USER_EMAIL")
PASSWORD = os.getenv("TEST_USER_PASSWORD")

@pytest.mark.smoke
def test_login():
    payload = {
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    }
    response = requests.post(f"{BASE_URL}/users/login", json=payload)
    
    assert response.status_code == 200
    assert "token" in response.json()["user"]