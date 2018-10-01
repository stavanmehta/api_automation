from main.apiclient import APIClient
from main.uris import LOGIN_URI


class Login(APIClient):
    def __init__(self):
        """
        Initialize Login class
        """
        super(Login, self).__init__()
        self.token = None

    def login(self, username=None, password=None):
        """
        login with username and password.
        If username or password is None, it will try to make a GET request, otherwise, make POST request
        :param username: <str>
        :param password: <str>
        :return: <dict> response dictionary
        """
        payload = {'username': username, 'password': password}
        if not username or not password:
            login_response = self.get(LOGIN_URI)
            return login_response
        else:
            login_response = self.post("/login", request_payload=payload)
            self.token = login_response.get("text").get("token")
            return login_response

    def get_token(self):
        """
        Get generated token for Login Instance
        :return: <str>
        """
        return self.token
