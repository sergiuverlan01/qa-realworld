from api.base_client import BaseClient


class AuthClient(BaseClient):
    """
    Client pentru autentificare.
    Mosteneste din BaseClient - are acces la get, post, put, delete, set_auth_token.
    """

    def register(self, username: str, email: str, password: str):
        """
        Inregistreaza un user nou.
        POST /api/users
        """
        payload = {
            "user": {
                "username": username,
                "email": email,
                "password": password
            }
        }
        return self.post("/users", payload=payload)

    def login(self, email: str, password: str):
        """
        Logheaza un user existent si seteaza automat token-ul in sesiune.
        POST /api/users/login
        """
        payload = {
            "user": {
                "email": email,
                "password": password
            }
        }
        response = self.post("/users/login", payload=payload)

        # Daca loginul a reusit, seteaza automat token-ul pentru requesturile viitoare
        if response.status_code == 200:
            token = response.json()["user"]["token"]
            self.set_auth_token(token)

        return response

    def get_current_user(self):
        """
        Returneaza datele userului autentificat curent.
        GET /api/user
        Necesita autentificare.
        """
        return self.get("/user")

    def update_user(self, **fields):
        """
        Actualizeaza datele userului curent.
        PUT /api/user
        Necesita autentificare.

        Exemplu: update_user(bio="New bio", image="http://...")
        """
        payload = {"user": fields}
        return self.put("/user", payload=payload)

    def logout(self):
        """
        Sterge token-ul din sesiune.
        Nu exista endpoint de logout in Conduit API - doar stergem token-ul local.
        """
        self.clear_auth_token()