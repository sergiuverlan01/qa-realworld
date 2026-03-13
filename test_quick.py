import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("TEST_USER_EMAIL")
PASSWORD = os.getenv("TEST_USER_PASSWORD")

# PASUL 1: Login
print("\n=== STEP 1: LOGIN ===")
login_payload = {
    "user": {
        "email": EMAIL,
        "password": PASSWORD
    }
}

response = requests.post(
    f"{BASE_URL}/users/login",
    json=login_payload,
    headers={"Content-Type": "application/json"}
)

print(f"Status code: {response.status_code}")
print(f"Response: {response.json()}")

# PASUL 2: Extrage token-ul
print("\n=== STEP 2: RETRIEVE TOKEN ===")
token = response.json()["user"]["token"]
print(f"Token primit: {token[:30]}...")  # afisam doar primele 30 caractere

# PASUL 3: GET /api/user cu token
print("\n=== STEP 3: GET CURRENT USER ===")
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {token}"
}

user_response = requests.get(
    f"{BASE_URL}/user",
    headers=headers
)

print(f"Status code: {user_response.status_code}")
print(f"User data: {user_response.json()}")