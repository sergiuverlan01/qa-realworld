import os
import requests
from dotenv import load_dotenv

load_dotenv()


class BaseClient:
    """
    Clasa de baza pentru toate requesturile HTTP.
    Toti ceilalti clienti mostenesc din aceasta clasa.
    """

    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://api.realworld.show/api")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, **kwargs)
        return response

    def post(self, endpoint: str, payload: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=payload, **kwargs)
        return response

    def put(self, endpoint: str, payload: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=payload, **kwargs)
        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, **kwargs)
        return response

    def set_auth_token(self, token: str):
        self.session.headers.update({
            "Authorization": f"Token {token}"
        })

    def clear_auth_token(self):
        self.session.headers.pop("Authorization", None)