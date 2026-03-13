from api.auth_client import AuthClient
def test_user():
    client= AuthClient()
    client.login(email="sergiu_verlan1993@yahoo.com", password="test1234!")
    rs = client.get("/user")
    data = rs.json()
    print(data)
    assert rs.status_code == 200
    