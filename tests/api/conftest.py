import pytest
from api.auth_client import AuthClient
from utils.data_factory import generate_user


@pytest.fixture(scope="session")
def registered_user():
    """
    Creeaza un user nou o singura data per sesiune de teste.
    Returneaza datele userului (username, email, password).
    """
    client = AuthClient()
    user_data = generate_user()

    response = client.register(
        username=user_data["username"],
        email=user_data["email"],
        password=user_data["password"]
    )

    assert response.status_code == 201, f"Register failed: {response.json()}"

    return user_data


@pytest.fixture(scope="session")
def auth_client(registered_user):
    """
    Returneaza un AuthClient autentificat.
    Foloseste userul creat de fixture-ul registered_user.
    """
    client = AuthClient()
    response = client.login(
        email=registered_user["email"],
        password=registered_user["password"]
    )

    assert response.status_code == 200, f"Login failed: {response.json()}"

    return client