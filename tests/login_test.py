import pytest as pytest

from main.features.login import Login

valid_users = [
    ("AdventurousEater", "1234", 200),
    ("PickyEater", "secret", 200)
]

invalid_users = [
    (None, None, 405, "Method not allowed. Make a POST request with a valid username and password"),
    ("AdventurousEater", None, 405, "Method not allowed. Make a POST request with a valid username and password"),
    (None, 1234, 405, "Method not allowed. Make a POST request with a valid username and password"),
    ("invalid-user", "1234", 401, "Unauthorized"),
    ("AdventurousEater", "invalid-password", 401, "Unauthorized"),
    ("invalid-user", "invalid-password", 401, "Unauthorized"),
]


@pytest.fixture(scope="module")
def login_fixture():
    login = Login()
    return login


@pytest.mark.parametrize("username, password, expected_status_code, expected_error", invalid_users)
def test_invalid_users(login_fixture, username, password, expected_status_code, expected_error):
    response = login_fixture.login(username, password)
    assert response.get("status_code") == expected_status_code
    assert response.get("text").get("error") == expected_error


@pytest.mark.parametrize("username, password, expected_status_code", valid_users)
def test_valid_users(login_fixture, username, password, expected_status_code):
    response = login_fixture.login(username, password)
    assert response.get("status_code") == expected_status_code
    assert login_fixture.get_token() is not None
    assert isinstance(login_fixture.get_token(), str)
